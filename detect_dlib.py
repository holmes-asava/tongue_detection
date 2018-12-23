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
    nose_above=(0,0)
    nose_below=(0,0)
    mouth_left=(0,0)
    mouth_right=(0,0)
    state_normal =1
    state_error   =0
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
    def detect_face(self,frame):
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        rects = self.detector(gray,0)
       
        if len(rects)!=1 :
            return self.state_error,frame,0,0,1,1,0,0

        else:   
            rect = rects[0]
            shape =  self.predictor(gray, rect)
            shape = face_utils.shape_to_np(shape) 
            self.nose_above=(int(shape[27][0]),int(shape[27][1]))
            self.nose_below=(int(shape[30][0]),int(shape[30][1]))
            self.mouth_left=(int(shape[60][0]),int(shape[60][1]))
            self.mouth_right=(int(shape[64][0]),int(shape[64][1]))
            (self.x,self.y,self.w,self.h) = face_utils.rect_to_bb(rect)
            cv2.rectangle(frame, (self.x,self.y), (self.x + self.w, self.y + self.h), (255, 255,255), 2)    
            face_roi_color=frame[self.y:self.y+self.h,self.x:self.x+self.w]
            self.mid_mouth_x=round((self.mouth_left[0]+self.mouth_right[0])/2)
            self.mid_mouth_y=self.nose_below[1]
            #cv2.circle(frame, (self.nose_below),2, (0, 0, 0), 4)
            if(self.x<0):
                print(self.x)
                return self.state_error,frame,0,0,1,1,0,0
            else:
                return self.state_normal,face_roi_color,self.x,self.y,self.w,self.h,self.mid_mouth_x,self.mid_mouth_y
           
    