import sys
import os
#import glob
import random
import threading
import time

from wallpaper import set_wallpaper
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QFileDialog

from window import Ui_mainWindow

directory = ""
run = False

class MainWindow(QtWidgets.QMainWindow, Ui_mainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.frame_timer.setEnabled(False)
        self.button_run_stop.clicked.connect(self.run_button)
        self.button_browse.clicked.connect(self.browse)
        self.img_led.setEnabled(False)

    def run_button(self):
        global run

        if (self.button_run_stop.text() == "RUN"):
            #print(self.timer_box.text()+self.comboBox_unit.currentText())
            run = True
            self.img_led.setEnabled(True)
            self.button_run_stop.setText("STOP")
            thd_countdown = threading.Thread(target=self.countdown)
            thd_countdown.start()
            #print(111)

        else :
            run = False
            self.img_led.setEnabled(False)
            self.button_run_stop.setText("RUN")
            #print(333)

    def browse(self):
        global directory

        #fname = QFileDialog.getOpenFileName(self, 'Open file','c:\\',
        #"Image files (*.jpg *.png)")
        fname = QFileDialog()
        fname.setFileMode(QFileDialog.Directory)
        fname.setOption(QFileDialog.ShowDirsOnly, True)
        #fname.setFilter("Image files (*.jpg)")
        #fname.exec()
        directory = fname.getExistingDirectory() # Get the choosen dir
        directory = os.path.normpath(directory)
        #imgCounter = len(glob.glob1(directory,"*.jpg"))
        #imgCounter = imgCounter + len(glob.glob1(directory,"*.png"))

        self.label_info_browse.setText(
            f"Path : {directory}\n\nImages found = {self.imgCount()}")
        
        self.frame_timer.setEnabled(True)
        
        #self.wallpaperize(directory)
    
    def imgCount(self):
        global directory

        imgs = len([f for f in os.listdir(directory)
        if f.endswith('.jpg')
        or f.endswith('jpeg')
        or f.endswith('png')
        and os.path.isfile(os.path.join(directory, f))])

        return imgs
    
    def countdown(self):
        global directory

        t_init = int(self.timer_box.text())
        t = t_init
        unit = self.comboBox_unit.currentText()

        if unit == "Min.":
            t = t * 60

        while run:
            while t and run == True:
                mins, secs = divmod(t, 60)
                timer = 'Next wallpaper in : {:02d}:{:02d}'.format(mins, secs)
                self.label_info_timer.setText(f"{timer} \n\nDisplayed : 4" )
                #print(timer, end="\r")
                time.sleep(1)
                t -= 1
            self.wallpaperize(directory)
            print("FINISH")
            t = t_init


    def wallpaperize(self, path):
        x = random.choice(os.listdir(path))

        path = os.path.join(path, x)
        #target = f"{path}\\{x}"
        #target = target.replace("/", "\\")
        #print(path)
        set_wallpaper(path)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())