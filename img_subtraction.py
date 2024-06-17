import cv2
import time
import datetime
import threading
import os

folder_path = r"C:\Users\pantn\VigilantCam\IMG_SUB_SCREENSHOT"
if not os.path.exists(folder_path):
    print("Folder does not exist. Creating folder...")
    os.makedirs(folder_path)
def subtraction():

    global last_screenshot_time
    background = None  # Initialize background variable
    last_screenshot_time = 0  # Variable to track the time when the last screenshot was captured

    def take_screenshot(frame, name):
        global last_screenshot_time
        current_time = time.time()
        if current_time - last_screenshot_time > 10:  # Check if 10 seconds have passed since the last screenshot
            current_time_str = datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
            ss_path = os.path.join(folder_path, f"{current_time_str}.jpg")
            cv2.imwrite(ss_path, frame)
            print("Screenshot captured!")
            last_screenshot_time = current_time  # Update the last screenshot time

    def capture_initial_state(cap):
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to capture frame")
            return None
        return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    def detect_change(frame, initial_state, threshold=50000):
        global background
        # Convert the frame to grayscale for background subtraction
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Resize the current frame to match the dimensions of the initial state frame
        gray_resized = cv2.resize(gray, (initial_state.shape[1], initial_state.shape[0]))

        # Apply Gaussian blur to reduce noise
        gray_blur = cv2.GaussianBlur(gray_resized, (21, 21), 0)

        # Compute absolute difference between the current frame and the initial state
        frame_diff = cv2.absdiff(initial_state, gray_blur)

        # Apply threshold to highlight significant changes
        _, thresh = cv2.threshold(frame_diff, 30, 255, cv2.THRESH_BINARY)

        # Count non-zero pixels in the thresholded image
        count = cv2.countNonZero(thresh)

        return count > threshold, frame_diff

    def countdown():
        for i in range(10, 0, -1):
            time.sleep(1)

    cap = cv2.VideoCapture(0)
    initial_state = capture_initial_state(cap)
    countdown_thread = threading.Thread(target=countdown)
    countdown_thread_started = False

    while True:
        if initial_state is None:
            print("Error: Failed to capture initial state")
            break

        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to capture frame")
            break

        is_change, frame_diff = detect_change(frame, initial_state)

        # Display the camera feed
        cv2.imshow("Camera Feed", frame)

        # Display the detected changes
        cv2.imshow("Detected Changes", frame_diff)

        if is_change:
            take_screenshot(frame, "changed")
            if not countdown_thread_started:  # Start countdown thread only if it's not already started
                countdown_thread.start()
                countdown_thread_started = True

            # Reset the initial state by capturing a new frame
            initial_state = capture_initial_state(cap)
            if initial_state is None:
                print("Error: Failed to capture initial state")
                break

        # Check for exit command
        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
