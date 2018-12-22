# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Pin Hole Camera\test\Gui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets  
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import cv2
from detect_color import detect_color
from detect_dlib  import detect_dlib
from circle_detection import circle_detection
import matplotlib.pyplot as plt
import numpy as np
import scipy.signal
detectdlib   = detect_dlib()
detectcolor = detect_color()
detectcircle= circle_detection()
class Ui_MainWindow(object):
    data_x=[]
    data_y=[]
    #dimeter is mean radias
    radius_ref = 25
    max_x=0
    min_x=0
    max_y=0
    min_y=0
    def setupUi(self, MainWindow):
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1120, 642)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.checkBox_Topbottom = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_Topbottom.setGeometry(QtCore.QRect(760, 200, 81, 17))
        self.checkBox_Topbottom.setObjectName("checkBox_Topbottom")
        self.checkBox_Leftright = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_Leftright.setGeometry(QtCore.QRect(910, 200, 81, 17))
        self.checkBox_Leftright.setObjectName("checkBox_Leftright")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(760, 360, 113, 20))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(950, 360, 121, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.max_top = QtWidgets.QLabel(self.centralwidget)
        self.max_top.setGeometry(QtCore.QRect(760, 340, 47, 13))
        self.max_top.setObjectName("max_top")
        self.max_bottom = QtWidgets.QLabel(self.centralwidget)
        self.max_bottom.setGeometry(QtCore.QRect(760, 420, 71, 16))
        self.max_bottom.setObjectName("max_bottom")
        self.max_right = QtWidgets.QLabel(self.centralwidget)
        self.max_right.setGeometry(QtCore.QRect(950, 420, 47, 13))
        self.max_right.setObjectName("max_right")
        self.max_left = QtWidgets.QLabel(self.centralwidget)
        self.max_left.setGeometry(QtCore.QRect(950, 340, 47, 13))
        self.max_left.setObjectName("max_left")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(760, 440, 113, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(950, 440, 113, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.video = QtWidgets.QLabel(self.centralwidget)
        self.video.setGeometry(QtCore.QRect(20, 30, 640, 480))
        self.video.setFrameShape(QtWidgets.QFrame.Box)
        self.video.setText("")
        self.video.setObjectName("video")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(720, 560, 371, 25))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.setpushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.setpushButton.setObjectName("setpushButton")
        self.horizontalLayout.addWidget(self.setpushButton)
        self.startButton = QtWidgets.QPushButton(self.layoutWidget)
        self.startButton.setObjectName("startButton")
        self.startButton.setCheckable(True)
        
        self.horizontalLayout.addWidget(self.startButton)
        self.stopButton = QtWidgets.QPushButton(self.layoutWidget)
        self.stopButton.setObjectName("stopButton")
        self.horizontalLayout.addWidget(self.stopButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1120, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.startButton.setEnabled(False)
        self.stopButton.setEnabled(False)
        self.state_topbottom = 1
        self.state_leftright = 1
        self.checkBox_Topbottom.toggle()
        self.checkBox_Leftright.toggle()
        self.checkBox_Topbottom.stateChanged.connect(self.state_TopBottom)
        self.checkBox_Leftright.stateChanged.connect(self.state_LeftRight)


        
        self.image=None
        
        self.start_video()
        self.stopButton.clicked.connect(self.stop_rec)
        self.state_rec=0
        self.startButton.clicked.connect(self.start_rec)
        self.setpushButton.clicked.connect(self.initial_record)
    
 
    def state_TopBottom(self, int):
        if self.checkBox_Topbottom.isChecked():
            self.lineEdit.setEnabled(True)
            self.lineEdit_3.setEnabled(True)
            self.state_topbottom = 1
        else:
           self.lineEdit.setEnabled(False)
           self.lineEdit_3.setEnabled(False)
           self.state_topbottom = 0

    def state_LeftRight(self, int):
        if self.checkBox_Leftright.isChecked():
            self.lineEdit_2.setEnabled(True)
            self.lineEdit_4.setEnabled(True)
            self.state_leftright = 1
        else:
           self.lineEdit_2.setEnabled(False)
           self.lineEdit_4.setEnabled(False)
           self.state_leftright = 0

    def initial_record(self):
        self.r =detectcircle.return_center()
        if self.r!= -1:
            self.startButton.setEnabled(True)
            self.stopButton.setEnabled(False)
            self.setpushButton.setEnabled(True)
            self.ref_x=0
            self.ref_y=0
            
    def start_rec(self):
        self.max_x=0
        self.min_x=0
        self.max_x=0    
        self.min_y=0
        self.data_x=[]
        self.data_y=[]
        self.state_rec=1
        if(self.state_topbottom):
                        
            self.lineEdit_3.setText("0")
            self.lineEdit.setText("0")
            
        if(self.state_leftright): 
                        
            self.lineEdit_2.setText("0")
            self.lineEdit_4.setText("0")                
            
        self.startButton.setEnabled(False)
        self.stopButton.setEnabled(True)
        self.setpushButton.setEnabled(False)

    def stop_rec(self):
        self.state_rec=0
        self.startButton.setEnabled(True)
        self.stopButton.setEnabled(False)
        self.setpushButton.setEnabled(True)
        #filter
        x_sm = np.array(self.data_x)
        y_sm = np.array(self.data_x)
        xnew = scipy.signal.savgol_filter(x_sm, 5, 3)
        ynew = scipy.signal.savgol_filter(y_sm, 5, 3)
        #x_smooth = np.linspace(x_sm.min(), x_sm.max(), 200)
        #y_smooth = spline(x, y, x_smooth)
        plt.plot(xnew)
        plt.show()
        plt.plot(ynew)
        plt.show()
       
    def stop_vdo(self):
        self.timer.stop()
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.checkBox_Topbottom.setText(_translate("MainWindow", "Top - Bottom"))
        self.checkBox_Leftright.setText(_translate("MainWindow", "Left - Right"))
        self.max_top.setText(_translate("MainWindow", "Max. top"))
        self.max_bottom.setText(_translate("MainWindow", "Max. bottom"))
        self.max_right.setText(_translate("MainWindow", "Max. right"))
        self.max_left.setText(_translate("MainWindow", "Max. left"))
        self.setpushButton.setText(_translate("MainWindow", "SET"))
        self.startButton.setText(_translate("MainWindow", "START"))
        self.stopButton.setText(_translate("MainWindow", "STOP"))
        
    def changeTitle(self, state):
        _translate = QtCore.QCoreApplication.translate
        if state == Qt.Checked:
            self.lineEdit.setText(_translate("MainWindow", "hello"))
            print("check")
        else:
            self.lineEdit.setText(_translate("MainWindow", "555"))
            print("uncheck")

    def start_video(self):
        
       
        self.capture = detectcolor.cap
        

        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT,480)
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH,640)
        
        self.timer=QTimer()
        
        self.timer.timeout.connect(self.update_frame)
        
        self.timer.start(16)
        

    def update_frame(self):
        try:
            self.image= detectcolor.open_camera()
            #dlib a'Home
            state,self.face,x,y,h,w,midx,midy=detectdlib.detect_face(self.image)
            if state==1:
                
                output= detectcolor.detect(self.face)
                output,cx,cy = detectcolor.center(output,self.image,x,y)
                output = detectcircle.detect_circle(output)
            
                
                #self.image=cv2.flip(self.image,1)
                
                
                self.displayImage(output,1)
                
                if  (0<self.state_rec<11):
                    cur_x=(cx-midx)*self.radius_ref/self.r
                    cur_y=(cy-midy)*self.radius_ref/self.r
                    self.ref_x=cur_x+self.ref_x
                    self.ref_y=cur_y+self.ref_y
                    self.state_rec=self.state_rec+1
                    
                elif(self.state_rec==11):
                    self.ref_x=self.ref_x/10
                    self.ref_y=self.ref_y/10
                    cur_x=(cx-midx)*self.radius_ref/self.r
                    cur_y=(cy-midy)*self.radius_ref/self.r
                    if(cur_x>self.max_x):
                        if(abs(cur_x-self.ref_x)<50):
                            self.max_x=cur_x
                    if(cur_x<self.min_x):
                        if(abs(cur_x-self.ref_x)<50):
                            self.min_x=cur_x
                    if(cur_y>self.max_y):
                        if(abs(cur_y-self.ref_y)<50):
                            self.max_y=cur_y
                    if(cur_y<self.min_y):
                        if(abs(cur_y-self.ref_y)<50):
                           self.min_y=cur_y
                    
                    if(self.state_topbottom):
                        self.lineEdit_3.setText("%.2f" %(self.max_y))
                        self.lineEdit.setText("%.2f" %(abs(self.min_y)))
                        self.data_y.append(-cur_y)
                    if(self.state_leftright): 
                        self.lineEdit_2.setText("%.2f" %(abs(self.min_x)))
                        self.lineEdit_4.setText("%.2f" %(self.max_x))                  
                        self.data_x.append(cur_x)
                    self.old_x=cur_x
                    self.old_y=cur_y
                    state_rec=12
                elif(self.state_rec==12):
                    if cx ==0 or cy==0:
                        cur_x=self.old_x
                        cur_y=self.old_y
                    else:
                        cur_x=(cx-midx)*self.radius_ref/self.r
                        cur_y=(cy-midy)*self.radius_ref/self.r

                    if(cur_x>self.max_x):
                        if(abs(cur_x-self.ref_x)<50):
                            self.max_x=cur_x
                        else:
                            cur_x= self.old_x
                          
                    if(cur_x<self.min_x):
                        if(abs(cur_x-self.ref_x)<50):
                            self.min_x=cur_x
                        else:
                            cur_x= self.old_x
                    if(cur_y>self.max_y):
                        if(abs(cur_y-self.ref_y)<50):
                            self.max_y=cur_y
                        else:
                            cur_y= self.old_y   
                    if(cur_y<self.min_y):
                        if(abs(cur_y-self.ref_y)<50):
                           self.min_y=cur_y
                        else:
                            cur_y= self.old_y
                    if(self.state_topbottom):
                        
                        self.lineEdit_3.setText("%.2f" %(self.max_y))
                        self.lineEdit.setText("%.2f"%(abs(self.min_y)))
                        self.data_y.append(-cur_y)
                    if(self.state_leftright): 
                        
                        self.lineEdit_2.setText("%.2f"%(self.max_x))
                        self.lineEdit_4.setText("%.2f"%(abs(self.min_x)))                
                        self.data_x.append(cur_x)
                    
                    self.old_x=cur_x
                    self.old_y=cur_y
                
                
                
                    
                    
            else:
                self.displayImage(self.face,1)
        except:
            pass

    def displayImage(self,imag,window=1):
        """
        cv2.ellipse(imag, (320, 240), (90, 150), 0, 0, 360, (255,255,255), 2)
        cv2.line(imag,(270,300),(360,300),(255,255,255),1)
        cv2.line(imag,(320,280),(320,320),(255,255,255),1)
        """
        rgbImage = cv2.cvtColor(imag, cv2.COLOR_BGR2RGB)
        self.convertToQtFormat = QImage(rgbImage.data, rgbImage.shape[1], rgbImage.shape[0], QImage.Format_RGB888)
        
        pixmap = QPixmap(QPixmap.fromImage(self.convertToQtFormat))
        
        #video = QLabel()
        
        #video.setPixmap(pixmap)

        p = self.convertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
        
        if window==1:
            
            self.video.setPixmap(QPixmap.fromImage(p))
            
            self.video.mousePressEvent = self.getPixel
            
           
            #self.video.setScaledContents(true)
            

    def getPixel(self, event):
        print("getPixel")
        x = event.pos().x()
        y = event.pos().y()
        c = self.convertToQtFormat.pixel(x,y)  # color code (integer): 3235912
        # depending on what kind of value you like (arbitary examples)
        c_qobj = QColor(c)  # color object
        c_rgb = QColor(c).getRgb()  # 8bit RGBA: (255, 23, 0, 255)
        if self.state_rec == 0:
            detectcolor.cal_color_boundaries_one_point(c_rgb[0],c_rgb[1],c_rgb[2])
        #c_rgbf = QColor(c).getRgbf()  # RGBA float: (1.0, 0.3123, 0.0, 1.0)
        
       
                  
        
   
            
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

