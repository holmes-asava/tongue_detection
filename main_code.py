import cv2
import imutils
#from detect_color import detect_color as a #เอาตัวแปรมารับclassได้เลย
#from detect_color import detect_color
from detect_color import detect_color
from circle_detection import detect_circle
'''
a  = detect_color()
print(a.color_boundaries)
a.hmin = 30
a.cal_color_boundaries()
print(a.color_boundaries)
'''
detectcolor = detect_color()


while(1):
    frame = detectcolor.open_camera()
    #output = detect_circle(frame)
    detectcolor.auto = False
    detectcolor.open_cv_window()
    '''
    detectcolor.frame = frame
    detectcolor.auto = False
    detectcolor.checkmouse()
    '''   
    output = detectcolor.detect(frame)
    output = detectcolor.center(output,frame)
    cv2.imshow('output',output)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
