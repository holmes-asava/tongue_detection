import cv2
import imutils
#from detect_color import detect_color as a #เอาตัวแปรมารับclassได้เลย
#from detect_color import detect_color
from detect_color import detect_color
from circle_detection import circle_detection
from detect_dlib import detect_dlib
'''
a  = detect_color()
print(a.color_boundaries)
a.hmin = 30
a.cal_color_boundaries()
print(a.color_boundaries)
'''
detectcolor = detect_color()
detectdlib = detect_dlib()
detectcircle= circle_detection()
while(1):
    frame = detectcolor.open_camera()
    
    detectcolor.auto = False
    detectcolor.open_cv_window()
    '''
    detectcolor.frame = frame
    detectcolor.auto = False
    detectcolor.checkmouse()
    '''   
    
    state,face_detect,x,y,w,h,midx,midy = detectdlib.detect_face(frame)
    output = detectcolor.detect(face_detect)
    output,cx,cy = detectcolor.center(output,frame,x,y)
    output = detectcircle.detect_circle(output)
    #cv2.imshow('face',face_detect)
    cv2.imshow('output',output)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
