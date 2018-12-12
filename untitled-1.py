import sys
import pyglet
import time
from multiprocessing import Process
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from untitled import Ui_MainWindow

class MyWidget(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.PlayButton.clicked.connect(self.play)
        self.PauseButton.clicked.connect(self.pause)
        self.MusicSlider.setMaximum(length)
        self.MusicSlider.valueChanged.connect(self.p)
        self.VolumeSlider.valueChanged.connect(self.change_volume)
        self.VolumeSlider.setValue(10)
        self.PlusButton.clicked.connect(self.plus)
        self.MinusButton.clicked.connect(self.minus)
        self.SpecialSlider.valueChanged.connect(self.t)
 
    def play(self):
        player.play()
        
    def pause(self):
        player.pause()
        
    def p(self, number):
        player.seek(number)
        
    def change_volume(self, number):
        player.volume = number / 10
        
    def change_time(self, number):
        self.TimeBrowser.setText('{}:{} | {}:{}'.format(number // 60, number % 60, length // 60, length % 60))
        
    def plus(self):
        shift = min(length, player.time + ARRAY[special_slider])
        player.seek(shift)
        self.MusicSlider.setValue(shift)
        
            
    def minus(self):
        shift = max(0, player.time - ARRAY[special_slider])
        player.seek(shift)
        self.MusicSlider.setValue(shift)        
        
    def t(self, number):
        global special_slider
        special_slider = number
        

special_slider = 0
ARRAY = [5, 15, 60, 300]
current_pos = 0
music = pyglet.media.load('Test.mp3')
length = music.duration
player = pyglet.media.Player()
player.queue(music)
app = QApplication(sys.argv)
ex = MyWidget()
ex.show()    
sys.exit(app.exec_())