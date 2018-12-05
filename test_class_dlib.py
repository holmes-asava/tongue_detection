import cv2
from detect_color import detect_color
from detect_dlib import detect_dlib
detectcolor = detect_color()
detectdlib = detect_dlib()

while(1):
    frame = detectcolor.open_camera()
    output = detectdlib.detect_face(frame)
    cv2.imshow('output',output)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
