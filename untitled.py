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
        MainWindow.resize(620, 285)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 620, 265))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.MinusButton = QtWidgets.QPushButton(self.tab)
        self.MinusButton.setGeometry(QtCore.QRect(460, 95, 30, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.MinusButton.setFont(font)
        self.MinusButton.setObjectName("MinusButton")
        self.PlusButton = QtWidgets.QPushButton(self.tab)
        self.PlusButton.setGeometry(QtCore.QRect(460, 30, 30, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.PlusButton.setFont(font)
        self.PlusButton.setObjectName("PlusButton")
        self.VerticalLine_4 = QtWidgets.QFrame(self.tab)
        self.VerticalLine_4.setGeometry(QtCore.QRect(600, 10, 20, 225))
        self.VerticalLine_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.VerticalLine_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.VerticalLine_4.setObjectName("VerticalLine_4")
        self.MusicLengthLabel = QtWidgets.QLabel(self.tab)
        self.MusicLengthLabel.setGeometry(QtCore.QRect(280, 115, 45, 18))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.MusicLengthLabel.setFont(font)
        self.MusicLengthLabel.setText("")
        self.MusicLengthLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.MusicLengthLabel.setObjectName("MusicLengthLabel")
        self.RewindLabel_2 = QtWidgets.QLabel(self.tab)
        self.RewindLabel_2.setGeometry(QtCore.QRect(395, 85, 50, 15))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.RewindLabel_2.setFont(font)
        self.RewindLabel_2.setObjectName("RewindLabel_2")
        self.StartTimeLabel = QtWidgets.QLabel(self.tab)
        self.StartTimeLabel.setGeometry(QtCore.QRect(25, 115, 45, 18))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.StartTimeLabel.setFont(font)
        self.StartTimeLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.StartTimeLabel.setObjectName("StartTimeLabel")
        self.VerticalLine_2 = QtWidgets.QFrame(self.tab)
        self.VerticalLine_2.setGeometry(QtCore.QRect(330, 10, 20, 135))
        self.VerticalLine_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.VerticalLine_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.VerticalLine_2.setObjectName("VerticalLine_2")
        self.MaxVolumeLabel = QtWidgets.QLabel(self.tab)
        self.MaxVolumeLabel.setGeometry(QtCore.QRect(550, 25, 60, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.MaxVolumeLabel.setFont(font)
        self.MaxVolumeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.MaxVolumeLabel.setObjectName("MaxVolumeLabel")
        self.HorizontalLine = QtWidgets.QFrame(self.tab)
        self.HorizontalLine.setGeometry(QtCore.QRect(10, 0, 600, 20))
        self.HorizontalLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.HorizontalLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.HorizontalLine.setObjectName("HorizontalLine")
        self.MuteLabel = QtWidgets.QLabel(self.tab)
        self.MuteLabel.setGeometry(QtCore.QRect(560, 115, 45, 15))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.MuteLabel.setFont(font)
        self.MuteLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.MuteLabel.setObjectName("MuteLabel")
        self.RewindSlider = QtWidgets.QSlider(self.tab)
        self.RewindSlider.setGeometry(QtCore.QRect(355, 25, 30, 105))
        self.RewindSlider.setMaximum(3)
        self.RewindSlider.setPageStep(1)
        self.RewindSlider.setOrientation(QtCore.Qt.Vertical)
        self.RewindSlider.setObjectName("RewindSlider")
        self.MusicSlider = QtWidgets.QSlider(self.tab)
        self.MusicSlider.setGeometry(QtCore.QRect(25, 70, 300, 45))
        self.MusicSlider.setOrientation(QtCore.Qt.Horizontal)
        self.MusicSlider.setObjectName("MusicSlider")
        self.HorizontalLine_2 = QtWidgets.QFrame(self.tab)
        self.HorizontalLine_2.setGeometry(QtCore.QRect(10, 135, 600, 20))
        self.HorizontalLine_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.HorizontalLine_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.HorizontalLine_2.setObjectName("HorizontalLine_2")
        self.VerticalLine_1 = QtWidgets.QFrame(self.tab)
        self.VerticalLine_1.setGeometry(QtCore.QRect(0, 10, 20, 225))
        self.VerticalLine_1.setFrameShape(QtWidgets.QFrame.VLine)
        self.VerticalLine_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.VerticalLine_1.setObjectName("VerticalLine_1")
        self.PauseButton = QtWidgets.QPushButton(self.tab)
        self.PauseButton.setEnabled(True)
        self.PauseButton.setGeometry(QtCore.QRect(95, 25, 60, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.PauseButton.setFont(font)
        self.PauseButton.setObjectName("PauseButton")
        self.VerticalLine_3 = QtWidgets.QFrame(self.tab)
        self.VerticalLine_3.setGeometry(QtCore.QRect(495, 10, 20, 135))
        self.VerticalLine_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.VerticalLine_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.VerticalLine_3.setObjectName("VerticalLine_3")
        self.RewindLabel_4 = QtWidgets.QLabel(self.tab)
        self.RewindLabel_4.setGeometry(QtCore.QRect(395, 25, 50, 15))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.RewindLabel_4.setFont(font)
        self.RewindLabel_4.setObjectName("RewindLabel_4")
        self.CurrentTimeBrowser = QtWidgets.QTextBrowser(self.tab)
        self.CurrentTimeBrowser.setGeometry(QtCore.QRect(235, 20, 90, 45))
        self.CurrentTimeBrowser.setObjectName("CurrentTimeBrowser")
        self.PlayButton = QtWidgets.QPushButton(self.tab)
        self.PlayButton.setEnabled(True)
        self.PlayButton.setGeometry(QtCore.QRect(25, 25, 60, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.PlayButton.setFont(font)
        self.PlayButton.setObjectName("PlayButton")
        self.RewindLabel_3 = QtWidgets.QLabel(self.tab)
        self.RewindLabel_3.setGeometry(QtCore.QRect(395, 55, 50, 15))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.RewindLabel_3.setFont(font)
        self.RewindLabel_3.setObjectName("RewindLabel_3")
        self.VolumeSlider = QtWidgets.QSlider(self.tab)
        self.VolumeSlider.setGeometry(QtCore.QRect(525, 25, 30, 105))
        self.VolumeSlider.setMaximum(10)
        self.VolumeSlider.setOrientation(QtCore.Qt.Vertical)
        self.VolumeSlider.setObjectName("VolumeSlider")
        self.RewindLabel_1 = QtWidgets.QLabel(self.tab)
        self.RewindLabel_1.setGeometry(QtCore.QRect(395, 115, 50, 15))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.RewindLabel_1.setFont(font)
        self.RewindLabel_1.setObjectName("RewindLabel_1")
        self.LoopButton = QtWidgets.QPushButton(self.tab)
        self.LoopButton.setEnabled(True)
        self.LoopButton.setGeometry(QtCore.QRect(165, 25, 60, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.LoopButton.setFont(font)
        self.LoopButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.LoopButton.setObjectName("LoopButton")
        self.CurrentTrackLabel = QtWidgets.QLabel(self.tab)
        self.CurrentTrackLabel.setGeometry(QtCore.QRect(245, 150, 130, 25))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.CurrentTrackLabel.setFont(font)
        self.CurrentTrackLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.CurrentTrackLabel.setObjectName("CurrentTrackLabel")
        self.PreviousTrackButton = QtWidgets.QPushButton(self.tab)
        self.PreviousTrackButton.setGeometry(QtCore.QRect(25, 190, 70, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.PreviousTrackButton.setFont(font)
        self.PreviousTrackButton.setObjectName("PreviousTrackButton")
        self.NextTrackButton = QtWidgets.QPushButton(self.tab)
        self.NextTrackButton.setGeometry(QtCore.QRect(105, 190, 70, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.NextTrackButton.setFont(font)
        self.NextTrackButton.setObjectName("NextTrackButton")
        self.textBrowser = QtWidgets.QTextBrowser(self.tab)
        self.textBrowser.setGeometry(QtCore.QRect(190, 190, 405, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textBrowser.setFont(font)
        self.textBrowser.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser.setObjectName("textBrowser")
        self.HorizontalLine_3 = QtWidgets.QFrame(self.tab)
        self.HorizontalLine_3.setGeometry(QtCore.QRect(10, 225, 600, 20))
        self.HorizontalLine_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.HorizontalLine_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.HorizontalLine_3.setObjectName("HorizontalLine_3")
        self.RefeshButton = QtWidgets.QPushButton(self.tab)
        self.RefeshButton.setGeometry(QtCore.QRect(25, 155, 150, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.RefeshButton.setFont(font)
        self.RefeshButton.setObjectName("RefeshButton")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(40, 510, 120, 80))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 620, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Player"))
        self.MinusButton.setText(_translate("MainWindow", "-"))
        self.PlusButton.setText(_translate("MainWindow", "+"))
        self.RewindLabel_2.setText(_translate("MainWindow", "15 sec"))
        self.StartTimeLabel.setText(_translate("MainWindow", "0:00"))
        self.MaxVolumeLabel.setText(_translate("MainWindow", "100%"))
        self.MuteLabel.setText(_translate("MainWindow", "Mute"))
        self.PauseButton.setText(_translate("MainWindow", "Pause"))
        self.RewindLabel_4.setText(_translate("MainWindow", "5 min"))
        self.CurrentTimeBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.PlayButton.setText(_translate("MainWindow", "Play"))
        self.RewindLabel_3.setText(_translate("MainWindow", "1 min"))
        self.RewindLabel_1.setText(_translate("MainWindow", "5 sec"))
        self.LoopButton.setText(_translate("MainWindow", "Loop"))
        self.CurrentTrackLabel.setText(_translate("MainWindow", "Current track"))
        self.PreviousTrackButton.setText(_translate("MainWindow", "Previous"))
        self.NextTrackButton.setText(_translate("MainWindow", "Next"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.RefeshButton.setText(_translate("MainWindow", "Refresh"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Player"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))