import cv2
from imutils import face_utils
import numpy as np
#import argparse
import imutils
import dlib
import math

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    raise IOError("Cannot open webcam")


eye_cascade = cv2.CascadeClassifier('haarcascade_mcs_nose.xml')


while True:
    ret, frame = cap.read()
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

  
    eye = eye_cascade.detectMultiScale(gray,2,5)
    for (x,y,w,h) in eye:
    
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
     
   
    cv2.namedWindow("Video")
    cv2.imshow("Video", frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
    

cv2.destroyAllWindows()
cap.release()
