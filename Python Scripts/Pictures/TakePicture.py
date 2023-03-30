#Works on both Android and Windows
#pip install opencv-python
import os
import cv2
import datetime

#Create a VideoCapture object
cap = cv2.VideoCapture(0)

#Check if the camera is opened
if not cap.isOpened():
    raise IOError("Cannot open the camera")

#Set the resolution to the maximum supported by the camera
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

#Take a single frame from the camera
ret, frame = cap.read()

#Check if the frame was successfully captured
if ret:
    #Get the script directory
    script_dir = os.path.dirname(__file__)

    #Get the current time and format it as a string
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")

    #Create the full path of the image file
    image_path = os.path.join(script_dir, "{}.png".format(timestamp))

    #Save the frame to the image file in PNG format
    cv2.imwrite(image_path, frame)

    #Release the VideoCapture object
    cap.release()

    print("Image saved to {}!".format(image_path))
else:
    print("Error: Could not capture image")
