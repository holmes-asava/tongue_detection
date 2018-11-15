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
    
#ap = argparse.ArgumentParser()
#ap.add_argument("-p","--shape-predictor", required=True,
#                help="path to facial landmark predictor")
#ap.add_argument("-i", "--image", required=True,
#                help="path to input image")
#args = vars(ap.parse_args())

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("C:\Users\homer\image\shape_predictor_68_face_landmarks.dat")
while True:
    ret, frame = cap.read()
    #frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
    frame = imutils.resize(frame, width=1000)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    rects = detector(gray, 0)
    for rect in rects:
        shape = predictor(gray, rect)
        shape = face_utils.shape_to_np(shape)
        
        (x, y, w, h) = face_utils.rect_to_bb(rect)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.circle(frame, (x,y), 3, (0,255,0), 2)
        
        #frame2 = gray[y:y+h, x:x+w]
        #print(x,y,w,h)
        #print(len(frame2),len(frame2[0]))
        #print("\n")
        #cv2.namedWindow("Face")
        #cv2.imshow("Face", frame2)
        #key = cv2.waitKey(1) & 0xFF
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            break
        for (x,y) in shape:
            cv2.circle(frame, (x,y), 1, (0,0,255), 2)
    
        nose1=(int(shape[27][0]),int(shape[27][1]))
        nose2=(int(shape[30][0]),int(shape[30][1]))
        cv2.line(frame,nose1,nose2,(0,255,0),2)
        eye1=(int(shape[36][0]),int(shape[36][1]))
        eye2=(int(shape[45][0]),int(shape[45][1]))
        cv2.line(frame,eye1,eye2,(0,255,0),2)
        
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            break

        x1=int(shape[36][0])
        y1=int(shape[36][1])
        x2=int(shape[45][0])
        y2=int(shape[45][1])
        disto=math.sqrt((math.fabs(x2-x1))**2+((math.fabs(y2-y1)))**2)
        distx=math.fabs(x2-x1)
    cv2.namedWindow("Video")
    cv2.imshow("Video", frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

cv2.destroyAllWindows()
cap.release()
