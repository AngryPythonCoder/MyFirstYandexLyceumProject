import sys
import os
import time
import json
import pyglet
import keyboard
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from untitled import Ui_MainWindow


def refresh(path):
    list_of_music = []
    if path is not None:
        for obj in os.listdir(path):
            if obj.split('.')[-1] == 'mp3' or obj.split('.')[-1] == 'wav':
                list_of_music.append(obj)
    return list_of_music

def activate_hotkeys(obj):        
    keyboard.add_hotkey(obj.hotkeys[0], obj.looping)
    keyboard.add_hotkey(obj.hotkeys[1], obj.play)
    keyboard.add_hotkey(obj.hotkeys[2], obj.pause)
    keyboard.add_hotkey(obj.hotkeys[3], lambda: obj.RewindSlider.setValue(min(3, obj.rewind_slider + 1)))
    keyboard.add_hotkey(obj.hotkeys[4], lambda: obj.RewindSlider.setValue(max(0, obj.rewind_slider - 1)))
    keyboard.add_hotkey(obj.hotkeys[5], obj.plus)
    keyboard.add_hotkey(obj.hotkeys[6], obj.minus)
    keyboard.add_hotkey(obj.hotkeys[7], obj.previous_track)
    keyboard.add_hotkey(obj.hotkeys[8], obj.next_track)
    keyboard.add_hotkey(obj.hotkeys[9], obj.refreshing)
    keyboard.add_hotkey(obj.hotkeys[10], lambda: obj.VolumeSlider.setValue(min(10, obj.player.volume * 10 + 1)))
    keyboard.add_hotkey(obj.hotkeys[11], lambda: obj.VolumeSlider.setValue(max(0, obj.player.volume * 10 - 1)))


class MyWidget(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.player = pyglet.media.Player()      
        self.current_pos = 0
        self.rewind_slider = 0
        self.status = 'Empty'
        self.loop = False
        self.hotkeys = []
        
        try:
            with open('music folder.json') as input_file:
                self.music_path = json.load(input_file)
        except FileNotFoundError:
            self.music_path = os.getcwd()
            with open('music folder.json', 'w') as output_file:
                json.dump(self.music_path, output_file)
                
        try:
            with open('hotkeys.json') as input_file:
                self.hotkeys = json.load(input_file)
        except FileNotFoundError:
            self.hotkeys = ['Num_' + str(i) for i in [j for j in range(10)] + ['Plus', 'Minus']]
            with open('hotkeys.json', 'w') as output_file:
                json.dump(self.hotkeys, output_file)            

        self.refreshing()
        self.VolumeSlider.setValue(10)
        self.MinusButton.clicked.connect(self.minus)
        self.PauseButton.clicked.connect(self.pause)
        self.PlayButton.clicked.connect(self.play)
        self.PlusButton.clicked.connect(self.plus)
        self.PreviousTrackButton.clicked.connect(self.previous_track)
        self.NextTrackButton.clicked.connect(self.next_track)
        self.RefreshButton.clicked.connect(self.refreshing)
        self.LoopButton.clicked.connect(self.looping)
        self.AcceptDirectoryButton.clicked.connect(self.directory)
        self.MusicSlider.valueChanged.connect(self.rewind)
        self.VolumeSlider.valueChanged.connect(self.change_volume)
        self.RewindSlider.valueChanged.connect(self.rewind_control)      
        self.Timer.timeout.connect(self.control_time)
        activate_hotkeys(self)
 
    def change_volume(self, number):
        self.player.volume = number / 10    
        
    def minus(self):
        shift = max(1, self.player.time - ARRAY[self.rewind_slider])
        self.player.seek(shift)
        self.MusicSlider.setValue(shift)   
        
    def play(self):
        if self.status == 'Empty':
            try:
                music = pyglet.media.load(self.music_path + '/' + self.list_of_music[0])
            except Exception:
                self.refreshing()
                music = pyglet.media.load(self.music_path + '/' + self.list_of_music[0])
            self.length = music.duration
            self.player.queue(music)
            self.MusicSlider.setMaximum(self.length)
            self.MusicLengthLabel.setText(str(int(self.length) // 60) + ':' + str(int(self.length) % 60).zfill(2))
            self.CurrentTrackBrowser.setText(self.list_of_music[0])
            self.status = 'Full'
        self.Timer.start()
        self.player.play()     
        
    def plus(self):
        shift = min(self.length, self.player.time + ARRAY[self.rewind_slider])
        self.player.seek(shift)
        self.MusicSlider.setValue(shift)    
        
    def pause(self):
        self.Timer.stop()
        self.player.pause()
        
    def rewind(self, number):
        if 0 < number:
            self.player.seek(number)
        else:
            self.player.seek(0.1)
        
    def rewind_control(self, number):
        self.rewind_slider = number
        
    def refreshing(self):
        self.list_of_music = refresh(self.music_path)
        
    def control_time(self):
        time = int(self.player.time)
        self.CurrentTimeBrowser.setText(str(time // 60) + ':' + str(time % 60).zfill(2))
        self.MusicSlider.setValue(time)
        if time == int(self.length):
            self.next_track(self.loop)
        
    def previous_track(self):
        self.list_of_music.insert(0, self.list_of_music[-1])
        self.list_of_music.pop(-1)
        self.CurrentTrackBrowser.setText(self.list_of_music[0])
        self.pause()
        self.status = 'Empty'
        self.play()
        self.rewind(0)      
        self.player.next_source()
        self.control_time() 
        
    def next_track(self, loop=False):
        if not loop:
            self.list_of_music.append(self.list_of_music[0])
            self.list_of_music.pop(0)
            self.CurrentTrackBrowser.setText(self.list_of_music[0])
            self.pause()
        self.status = 'Empty'
        self.play()
        self.rewind(0)       
        self.player.next_source()
        self.control_time()
    
    def directory(self):
        path = self.DirectoryEdit.text()
        old_path = self.music_path
        self.music_path = path
        try:
            self.refreshing()
            with open('music folder.json', 'w') as output_file:
                json.dump(self.music_path, output_file)    
        except Exception:
            self.music_path = old_path
            self.DirectoryEdit.setText('')
    
    def looping(self):
        self.loop = not self.loop
        if self.loop:
            self.LoopButton.setText('Looped')
        else:
            self.LoopButton.setText('Loop')
        

ARRAY = [5, 15, 60, 300]
app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
