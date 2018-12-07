import cv2
from imutils import face_utils
import numpy as np
import imutils
import dlib
from detect_color import detect_color

class detect_dlib(object):
    x=1
    y=1
    w=1
    h=1
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
    def detect_face(self,frame):
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        rects = self.detector(gray,0)
        for rect in rects:
            shape =  self.predictor(gray, rect)
            shape = face_utils.shape_to_np(shape) 
            (self.x,self.y,self.w,self.h) = face_utils.rect_to_bb(rect)
        cv2.rectangle(frame, (self.x,self.y), (self.x + self.w, self.y + self.h), (0, 255, 0), 2)    
        face_roi_color=frame[self.y:self.y+self.h,self.x:self.x+self.w]
        return face_roi_color,self.x,self.y,self.w,self.h
