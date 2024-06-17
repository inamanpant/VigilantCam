import tkinter as tk
from tkinter import ttk
import threading
from PIL import Image, ImageTk
from face_body_detect import face_body_detection
from img_subtraction import subtraction


class VigilantCAMApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("VigilantCAM")
        self.geometry("500x350")
        self.configure(bg="#F0F0F0")  # Set background color

        self.style = ttk.Style(self)
        self.style.configure('TFrame', background='#F0F0F0')  # Set background color for all ttk Frames

        self.create_widgets()

    def create_widgets(self):
        # Title label
        title_label = ttk.Label(self, text="Welcome to VigilantCAM", font=("Helvetica", 16, "bold"), background="#F0F0F0")
        title_label.pack(pady=20)

        # Image frame
        image_frame = ttk.Frame(self, style='TFrame')
        image_frame.pack()

        # Placeholder image for Face Detection
        self.placeholder_face_detection = self.load_image("placeholder_recording.png")
        label_face_detection = ttk.Label(image_frame, image=self.placeholder_face_detection, background="#F0F0F0")
        label_face_detection.grid(row=0, column=0, padx=10)

        # Start Face & Body Detection button
        btn_start_face_body_detection = ttk.Button(image_frame, text="Start Face & Body Detection", command=self.start_face_body_detection)
        btn_start_face_body_detection.grid(row=1, column=0, padx=20, pady=(0, 20))

        # Placeholder image for Image Subtraction
        self.placeholder_image_subtraction = self.load_image("placeholder_image_subtraction.png")
        label_image_subtraction = ttk.Label(image_frame, image=self.placeholder_image_subtraction, background="#F0F0F0")
        label_image_subtraction.grid(row=0, column=1, padx=10)

        # Start Image Subtraction button
        btn_start_image_subtraction = ttk.Button(image_frame, text="Start Image Subtraction", command=self.start_image_subtraction)
        btn_start_image_subtraction.grid(row=1, column=1, padx=20, pady=(0, 20))

        # New photo

    def load_image(self, image_path):
        img = Image.open(image_path)
        img = img.resize((180, 180), Image.LANCZOS)  # Use Image.LANCZOS for resizing
        photo = ImageTk.PhotoImage(img)
        return photo

    def start_face_body_detection(self):
        threading.Thread(target=face_body_detection, daemon=True).start()

    def start_image_subtraction(self):
        threading.Thread(target=subtraction, daemon=True).start()



if __name__ == "__main__":
    app = VigilantCAMApp()
    app.mainloop()
