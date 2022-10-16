# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'display.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1304, 526)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.pushbutton_play_pause = QtWidgets.QPushButton(self.centralwidget)
        self.pushbutton_play_pause.setObjectName("pushbutton_play_pause")
        self.gridLayout.addWidget(self.pushbutton_play_pause, 3, 0, 1, 2)
        self.obd_window = QtWidgets.QLabel(self.centralwidget)
        self.obd_window.setMinimumSize(QtCore.QSize(640, 360))
        self.obd_window.setMaximumSize(QtCore.QSize(640, 360))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.obd_window.setFont(font)
        self.obd_window.setAlignment(QtCore.Qt.AlignCenter)
        self.obd_window.setObjectName("obd_window")
        self.gridLayout.addWidget(self.obd_window, 1, 1, 1, 1)
        self.video_window = QtWidgets.QLabel(self.centralwidget)
        self.video_window.setEnabled(True)
        self.video_window.setMinimumSize(QtCore.QSize(640, 360))
        self.video_window.setMaximumSize(QtCore.QSize(640, 360))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        self.video_window.setFont(font)
        self.video_window.setAlignment(QtCore.Qt.AlignCenter)
        self.video_window.setObjectName("video_window")
        self.gridLayout.addWidget(self.video_window, 1, 0, 1, 1)
        self.pushbutton_record = QtWidgets.QPushButton(self.centralwidget)
        self.pushbutton_record.setObjectName("pushbutton_record")
        self.gridLayout.addWidget(self.pushbutton_record, 4, 0, 1, 2)
        self.pushbutton_exit = QtWidgets.QPushButton(self.centralwidget)
        self.pushbutton_exit.setObjectName("pushbutton_exit")
        self.gridLayout.addWidget(self.pushbutton_exit, 5, 0, 1, 2)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(640, 30))
        self.label.setMaximumSize(QtCore.QSize(640, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setMinimumSize(QtCore.QSize(640, 30))
        self.label_2.setMaximumSize(QtCore.QSize(640, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1304, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PythonObdPractice"))
        self.pushbutton_play_pause.setText(_translate("MainWindow", "Start"))
        self.obd_window.setText(_translate("MainWindow", "Object Detection Window"))
        self.video_window.setText(_translate("MainWindow", "Source Window"))
        self.pushbutton_record.setText(_translate("MainWindow", "Record"))
        self.pushbutton_exit.setText(_translate("MainWindow", "Exit"))
        self.label.setText(_translate("MainWindow", "原摄像头采集图像"))
        self.label_2.setText(_translate("MainWindow", "网络推理结果图像"))
