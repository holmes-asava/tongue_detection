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
class Ui_MainWindow(object):
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
        self.checkBox_Auto = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_Auto.setGeometry(QtCore.QRect(760, 150, 70, 17))
        self.checkBox_Auto.setObjectName("checkBox_Auto")
        self.checkBox_Custom = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_Custom.setGeometry(QtCore.QRect(910, 150, 70, 17))
        self.checkBox_Custom.setObjectName("checkBox_Custom")
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
        self.custom = QtWidgets.QLineEdit(self.centralwidget)
        self.custom.setGeometry(QtCore.QRect(990, 150, 41, 20))
        self.custom.setObjectName("custom")
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
        
        self.checkBox_Auto.toggle()
        self.checkBox_Auto.stateChanged.connect(self.changeTitle)
        self.image=None
        self.start_video()
        self.stopButton.clicked.connect(self.stop_video)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.checkBox_Topbottom.setText(_translate("MainWindow", "Top - Bottom"))
        self.checkBox_Leftright.setText(_translate("MainWindow", "Left - Right"))
        self.checkBox_Auto.setText(_translate("MainWindow", "Auto"))
        self.checkBox_Custom.setText(_translate("MainWindow", "Custom"))
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
        print("video")
        self.capture=cv2.VideoCapture(0)
        print("check1")

        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT,480)
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH,640)
        print("check2")
        self.timer=QTimer()
        print("check3")
        self.timer.timeout.connect(self.update_frame)
        print("check4")
        self.timer.start(5)

    def update_frame(self):
        ret,self.image=self.capture.read()
        print("fucK1")
        self.image=cv2.flip(self.image,1)
        print("fucK2")
        self.displayImage(self.image,1)
    
        print("fucK3")
    def stop_video(self):
        self.timer.stop()

    def displayImage(self,imag,window=1):
        
        rgbImage = cv2.cvtColor(imag, cv2.COLOR_BGR2RGB)
        convertToQtFormat = QImage(rgbImage.data, rgbImage.shape[1], rgbImage.shape[0], QImage.Format_RGB888)
        p = convertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
        
        if window==1:
            
            self.video.setPixmap(QPixmap.fromImage(p))
            print("Hello")
            #self.video.setScaledContents(true)
            print("window")
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

