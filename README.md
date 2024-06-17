#VigilantCam

VigilantCAM is a Python-based surveillance application that leverages computer vision techniques to detect faces and bodies in real-time and to identify significant changes in the video feed. The application features two main functionalities: Face & Body Detection and Image Subtraction.

Features-
1.Face & Body Detection:

Uses OpenCV's pre-trained classifiers to detect faces and bodies in real-time.
Records video when faces or bodies are detected.
Stops recording after a specified period of no detection.

2.Image Subtraction:

Captures initial frame and continuously monitors for significant changes.
Takes a screenshot when a substantial change is detected in the video feed.
Displays both the live camera feed and the detected changes.

Installation
To get started with VigilantCAM, follow these steps:

Clone the Repository:
git clone https://github.com/yourusername/VigilantCAM.git

cd VigilantCAM

Install Dependencies:
pip install -r requirements.txt

Ensure you have the following libraries installed:

tkinter
Pillow
OpenCV
numpy


Usage
Run the main.py file to start the application:
python main.py

Interface
The main interface has two primary sections:

Face & Body Detection: Click the "Start Face & Body Detection" button to begin detecting and recording faces and bodies.
Image Subtraction: Click the "Start Image Subtraction" button to start monitoring for significant changes in the video feed and capturing screenshots.

Hotkeys
Press q in the video feed window to stop the process.
