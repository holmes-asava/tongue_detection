# import the necessary packages
import numpy as np
import cv2
class circle_detection(object):
    r =None
    def detect_circle(self,frame):
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        gray_blur = cv2.GaussianBlur(gray, (15, 15), 0)
        #thresh = cv2.adaptiveThreshold(gray_blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV, 11, 1)
        #kernel = np.ones((3, 3), np.uint8)
        #closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=4)
        #output = gray_blur
        rows = gray.shape[0]
        circles = cv2.HoughCircles(gray_blur,cv2.HOUGH_GRADIENT,1, rows / 9,
                                param1=100, param2=40,
                                minRadius=10, maxRadius=70)
        if circles is not None:
            #print("circle")
            circles = np.round(circles[0, :]).astype("int")
            (x, y, self.r)=(circles[0,:])        
            cv2.circle(frame, (x, y),self.r, (0, 255, 0), 4)
            cv2.rectangle(frame, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
            return frame
        else:
            self.r = None
            return frame
    def return_center(self):
        if self.r is not None:
            return self.r
        else:
            return -1
    '''
cap = cv2.VideoCapture(0)
while(True):
    #read image
    ret, frame = cap.read()
    frame = cv2.flip(frame,1)
    output = frame.copy()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray_blur = cv2.GaussianBlur(gray, (15, 15), 0)
    output = gray_blur
    #thresh = cv2.adaptiveThreshold(gray_blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV, 11, 1)
    #kernel = np.ones((3, 3), np.uint8)
    #closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=4)
    #output = gray_blur
    rows = gray.shape[0]
    circles = cv2.HoughCircles(gray_blur,cv2.HOUGH_GRADIENT,1, rows / 9,
                               param1=100, param2=50,
                               minRadius=10, maxRadius=100)
    if circles is not None:
        print("circle")
        circles = np.round(circles[0, :]).astype("int")
        for (x, y, r) in circles:
            cv2.circle(output, (x, y), r, (0, 255, 0), 4)
            cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
    cv2.imshow('detected circles',output)
    cv2.imshow('real',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
'''