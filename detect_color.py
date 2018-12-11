import numpy as np
import cv2
import colorsys
import colorsys

class detect_color(object):
    #value for make HSV boundary-------------------------------
    hmin = 38
    hmax =80
    smin = 50
    smax = 200
    vmin = 50
    vmax = 200
    #------------------------------------------------------------
    auto = True # check auto if False use click_event and cal_color_boundaries function
    #variable for locate mouse click location ---------------------
    cor_x1 = 0
    cor_y1 = 0
    cor_x2 = 0
    cor_y2 = 0
    #--------------------------------------------------------------
    click = False # check mouse click
    #default HSV boundaries for detection
    color_boundaries = [
            ([hmin, smin, vmin], [hmax,smax, vmax])
    ]

    #open 1st time camera to declare variable
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    
    #open camera and return frame
    def open_camera(self):
        ret, self.frame = self.cap.read()
        self.frame = cv2.flip(self.frame,1)
        return self.frame

    #calc new HSV boundaries from area between 2 mouse click and plus/minus weight to lowest and highest
    
    def cal_color_boundaries(self):
        #height, width, channels = self.frame.shape
        #print(str(height)+"  "+str(width))
        frame = cv2.GaussianBlur(self.frame, (5, 5), 0)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        weight = 20
        weight1 = 0
        weight2 = 0
        weight3 = 0
        self.hmin = frame[self.cor_y1,self.cor_x1,0]
        self.hmax = frame[self.cor_y1,self.cor_x1,0]
        self.smin = frame[self.cor_y1,self.cor_x1,1]
        self.smax = frame[self.cor_y1,self.cor_x1,1]
        self.vmin = frame[self.cor_y1,self.cor_x1,2]
        self.vmax = frame[self.cor_y1,self.cor_x1,2] 
        
        if self.cor_x1 < self.cor_x2:
            x1 = self.cor_x1
            x2 = self.cor_x2
        elif self.cor_x1 > self.cor_x2:
            x1 = self.cor_x2
            x2 = self.cor_x1
        if self.cor_y1 < self.cor_y2:
            y1 = self.cor_y1
            y2 = self.cor_y2
        elif self.cor_y1 > self.cor_y2:
            y1 = self.cor_y2
            y2 = self.cor_y1
        for j in range(x1,x2):
            for i in range(y1,y2):
                h = self.frame[i,j,0]
                s = self.frame[i,j,1]
                v = self.frame[i,j,2]
                if h < self.hmin:
                    self.hmin = h
                elif h > self.hmax:
                    self.hmax = h
                if s < self.smin:
                    self.smin = s
                elif s > self.smax:
                    self.smax = s
                if v < self.vmin:
                    self.vmin = v
                elif v > self.vmax:
                    self.vmax = v
        
        self.color_boundaries = [
        ([np.clip(self.hmin - weight1,0,500), np.clip(self.smin- weight2,0,500), np.clip(self.vmin- weight3,0,500)], 
        [np.clip(self.hmax+ weight1,0,500), np.clip(self.smax+ weight2,0,500),np.clip(self.vmax+ weight3,0,500)])
        ]
        print(self.color_boundaries)
        cv2.destroyAllWindows()
        print("close window")
    
    def cal_color_boundaries_one_point(self,r,g,b):
        print(r)
        print(g)
        print(b)
        r = r/255
        g = g/255
        b = b/255
        print(r)
        print(g)
        print(b)
        smin = 50
        smax = 200
        vmin = 50
        vmax = 200
        h,s,v =colorsys.rgb_to_hsv(r, g, b)
        h=round(h*180)
        s=round(s*255)
        v=round(v*255)
        print(h)
        print(s)
        print(v)
        #blue_range = (95,130)
        #green_range =(38,80)
        #red_range = (165,180)
        if h in range(95,130):
            hmin = 95
            hmax = 130
        elif h in range(38,80):
            hmin = 38
            hmax = 80
        elif h in range(165,180):
            hmin = 165
            hmax = 180
        else:
            hmin = h -20
            hmax = h +20
        self.color_boundaries =[
        ([np.clip(hmin,0,255), np.clip(smin,0,255), np.clip(vmin,0,255)], 
        [np.clip(hmax,0,255), np.clip(smax,0,255),np.clip(vmax,0,255)])
        ]
        print("update color threshold:")
        print(self.color_boundaries)



    def cal_color(r,g,b):
        h,s,v = colorsys.rgb_to_hsv(r, g, b)
        return h,s,v
    
    def open_cv_window(self):
        cv2.imshow('real',self.frame)
        self.checkmouse()

    # collect location of mouse click
    def click_event(self,event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN and self.click == False:
            #print('click1')
            self.cor_x1 = x
            self.cor_y1 = y
            self.click = True
            #print(self.cor_x1)
            
        elif event == cv2.EVENT_LBUTTONDOWN and self.click == True:
            #print('click2')
            self.cor_x2 = x
            self.cor_y2 = y
            self.click = False
            #print(self.cor_x2)
            self.cal_color_boundaries()
            cv2.circle(self.frame, (y, x), 5, (255, 255, 255), -1)
            
    #if auto = False enable mouse function        
    def checkmouse(self):
        if self.auto == False:
            cv2.setMouseCallback("real",self.click_event)
        if self.click == True:
            cv2.circle(self.frame, (self.cor_y1, self.cor_x1), 5, (255, 255, 255), -1)
            cv2.putText(self.frame, "select1", (self.cor_y1-25, self.cor_x1-25),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
            cv2.imshow('real',self.frame)

    #detect color from HSV boundary and return  image
    def detect(self,frame):
        frame = cv2.GaussianBlur(frame, (5, 5), 0)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        boundaries = self.color_boundaries
        for (lower, upper) in boundaries:
            lower = np.array(lower, dtype = "uint8")
            upper = np.array(upper, dtype = "uint8")
            kernel_open = np.ones((10,10),np.uint8)
            kernel_close = np.ones((30,30),np.uint8)
            mask = cv2.inRange(frame, lower, upper)
            
            #mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel_open)
            #mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel_close)
            #mask = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

            output = cv2.bitwise_and(frame, frame, mask = mask)
            output_color_detec = cv2.cvtColor(output, cv2.COLOR_HSV2BGR)
            #ret,output_color_detec = cv2.threshold(output_color_detec,80,255,cv2.THRESH_BINARY)
            return output_color_detec

    def center(self,output,frame,x,y):
        output_color_detec = cv2.cvtColor(output, cv2.COLOR_BGR2GRAY)
        ret,thresh = cv2.threshold(output_color_detec,80,255,cv2.THRESH_BINARY)
        im2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

       # print(contours)
        #cv2.drawContours(frame, contours, -1, (0,255,0), 3)
        M = cv2.moments(thresh)
        try:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            cv2.circle(frame, (cX+x, cY+y), 5, (255, 255, 255), -1)
            cv2.putText(frame, "Mark", (cX + x - 25, cY + y - 25),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
            return frame,cX+x,cY+y
        except:
            return frame,0,0
        
''' 
-----------------------------------------Example Code-----------------------------------------------
import cv2
from detect_color import detect_color

detectcolor = detect_color()


while(1):
    frame = detectcolor.open_camera()
    detectcolor.auto = False
    detectcolor.checkmouse()
    detectcolor.frame = frame
    output = detectcolor.detect(frame)
    cv2.imshow('output',output)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
------------------------------------------------------------------------------------------------------------
'''