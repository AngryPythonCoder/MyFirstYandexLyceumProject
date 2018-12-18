import sys
import os
import time
import json
import pyglet
#from threading import Thread
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from untitled import Ui_MainWindow


#def refresh(path):
    #list_of_music = []
    #if path is not None:
        #for obj in os.listdir(path):
            #if obj.split('.')[-1] == 'mp3':
                #list_of_music.append(obj)
    #return list_of_music


class MyWidget(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.player = pyglet.media.Player()      
        self.current_pos = 0
        self.rewind_slider = 0
        self.status = 'Empty'
        
        #try:
            #with open('music folder.json') as input_file:
                #self.music_path = json.load(input_file)
        #except FileNotFoundError:
            #self.music_path = None
        #self.list_of_music = refresh(self.music_path)
        self.VolumeSlider.setValue(10)
        self.MinusButton.clicked.connect(self.minus)
        self.PauseButton.clicked.connect(self.pause)
        self.PlayButton.clicked.connect(self.play)
        self.PlusButton.clicked.connect(self.plus)
        self.MusicSlider.valueChanged.connect(self.rewind)
        self.VolumeSlider.valueChanged.connect(self.change_volume)
        self.RewindSlider.valueChanged.connect(self.rewind_control)           
 
    def change_volume(self, number):
        self.player.volume = number / 10    
        
    #def control_time(self):
        #while self.status == 'Empty':
            #time.sleep(1)
        #print(1)
        #while self.current_pos < self.length:
            #if self.status == 'Full':
                #self.current_pos = self.player.time
                #self.CurrentTimeBrowser.setText(str(int(self.current_pos) // 60) + ':' + str(int(self.current_pos) % 60).zfill(2))
            #time.sleep(1)
        
    def minus(self):
        shift = max(0, self.player.time - ARRAY[self.rewind_slider])
        self.player.seek(shift)
        self.MusicSlider.setValue(shift)   
        
    def play(self):
        if self.status == 'Empty':
            music = pyglet.media.load('Test.mp3')
            self.length = music.duration
            self.player.queue(music)
            self.MusicSlider.setMaximum(self.length)
            self.MusicLengthLabel.setText(str(int(self.length) // 60) + ':' + str(int(self.length) % 60).zfill(2))
            self.status = 'Full'
        self.player.play()     
        
    def plus(self):
        shift = min(self.length, self.player.time + ARRAY[self.rewind_slider])
        self.player.seek(shift)
        self.MusicSlider.setValue(shift)    
        
    def pause(self):
        self.player.pause()
        
    def rewind(self, number):
        self.player.seek(number)
        
    def rewind_control(self, number):
        self.rewind_slider = number
        

ARRAY = [5, 15, 60, 300]
app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
app.exec_()