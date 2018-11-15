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



ret,frame_previous = cap.read()
blur = cv2.medianBlur(frame_previous,7)
gray_previous=cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)

while True:
    ret, frame = cap.read()
    blur = cv2.medianBlur(frame,7)
    gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
    gray_diff=gray-gray_previous
    gray_previous=gray
    cv2.namedWindow("Video")
    cv2.imshow("Video", gray_diff)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
    

cv2.destroyAllWindows()
cap.release()
