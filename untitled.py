# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(340, 120)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.MusicSlider = QtWidgets.QSlider(self.centralwidget)
        self.MusicSlider.setGeometry(QtCore.QRect(20, 50, 200, 30))
        self.MusicSlider.setOrientation(QtCore.Qt.Horizontal)
        self.MusicSlider.setObjectName("MusicSlider")
        self.PlayButton = QtWidgets.QPushButton(self.centralwidget)
        self.PlayButton.setEnabled(True)
        self.PlayButton.setGeometry(QtCore.QRect(20, 20, 40, 20))
        self.PlayButton.setObjectName("PlayButton")
        self.PauseButton = QtWidgets.QPushButton(self.centralwidget)
        self.PauseButton.setEnabled(True)
        self.PauseButton.setGeometry(QtCore.QRect(70, 20, 40, 20))
        self.PauseButton.setObjectName("PauseButton")
        self.SpecialSlider = QtWidgets.QSlider(self.centralwidget)
        self.SpecialSlider.setGeometry(QtCore.QRect(230, 20, 20, 60))
        self.SpecialSlider.setMaximum(3)
        self.SpecialSlider.setOrientation(QtCore.Qt.Vertical)
        self.SpecialSlider.setObjectName("SpecialSlider")
        self.PlusButton = QtWidgets.QPushButton(self.centralwidget)
        self.PlusButton.setGeometry(QtCore.QRect(260, 20, 20, 20))
        self.PlusButton.setObjectName("PlusButton")
        self.MinusButton = QtWidgets.QPushButton(self.centralwidget)
        self.MinusButton.setGeometry(QtCore.QRect(260, 60, 20, 20))
        self.MinusButton.setObjectName("MinusButton")
        self.TimeBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.TimeBrowser.setGeometry(QtCore.QRect(130, 15, 90, 31))
        self.TimeBrowser.setObjectName("TimeBrowser")
        self.VolumeSlider = QtWidgets.QSlider(self.centralwidget)
        self.VolumeSlider.setGeometry(QtCore.QRect(300, 20, 20, 60))
        self.VolumeSlider.setMaximum(10)
        self.VolumeSlider.setOrientation(QtCore.Qt.Vertical)
        self.VolumeSlider.setObjectName("VolumeSlider")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 340, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.PlayButton.setText(_translate("MainWindow", "Play"))
        self.PauseButton.setText(_translate("MainWindow", "Pause"))
        self.PlusButton.setText(_translate("MainWindow", "+"))
        self.MinusButton.setText(_translate("MainWindow", "-"))
        self.TimeBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))

