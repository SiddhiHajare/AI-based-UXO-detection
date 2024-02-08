from pyimagesearch.motion_detection import SingleMotionDetector
from imutils.video import VideoStream
from flask import Response
from flask import Flask
from flask import render_template
import threading
import argparse
import datetime
import imutils
import time
import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

def detect(gray,frame):
    #use detectMultiScale by giving parameters: color, x scaling down, minimum zones to be accepted
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for(x,y,w,h) in faces:
        #to create a ref rectangle
        #parameters are the frame, upper left coord, lower right coord, color of box, thickness
        cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 2)
        roi_gray = gray[y:y+h, x:x+h]
        roi_color = frame[y:y+h, x:x+h]
    
#to reduce computing power, use eyes along with face
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 3)
        for(ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color, (ex,ey), (ex+ew,ey+eh), (0,255,0), 2)
            
    return frame

#face recognition with webcam

#to get the last frame of the webcam
#video_capture is an object created
video_capture = cv2.VideoCapture(0)

#run the webcam continuously till user interrupts
while(1):
    #to not read the first parameter
    #get the last frame of the webcam
    _, frame = video_capture.read()
    
    #gets an avg of BGR to get contrasting shades of gray
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    canvas = detect(gray, frame)
    
    #display all processed images in an animated window
    cv2.imshow('Video', canvas)
    
    #condition for exit
    #video stops if we press 'q'
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

outputFrame = None
lock = threading.Lock()
# initialize a flask object
app = Flask(__name__)
# initialize the video stream and allow the camera sensor to
# warmup
#vs = VideoStream(usePiCamera=1).start()
vs = VideoStream(src=0).start()
time.sleep(2.0)
#stop the webcam
video_capture.release()

#destroy all objects created
cv2.destroyAllWindows()