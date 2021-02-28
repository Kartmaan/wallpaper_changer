import sys
import os
import random
import threading
import time

from wallpaper import set_wallpaper
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QFileDialog

from window import Ui_mainWindow

__title__ = 'Wallpaper Changer'
__author__ = 'Kartmaan'
__version__ = '1.0'

directory = "" # Choosen directory
displayed = 0 # Wallpaper displayed
run = False

class MainWindow(QtWidgets.QMainWindow, Ui_mainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Buttons connection to their function
        self.button_run_stop.clicked.connect(self.runStop_button)
        self.button_browse.clicked.connect(self.browse)

        self.frame_timer.setEnabled(False)
        self.button_run_stop.setEnabled(False)
        self.img_led.setEnabled(False)

    def runStop_button(self):
        """ Run/Stop button behaviour
        A single button is used to start and stop the process"""

        global run, displayed

        # The process is not running
        # User wants to RUN the process
        if (self.button_run_stop.text() == "RUN"):
            run = True
            self.img_led.setEnabled(True)
            self.button_run_stop.setText("STOP")
            self.label_status.setText("")
            self.frame_browse.setEnabled(False)

            # Countdown thread
            thd_countdown = threading.Thread(target=self.countdown)
            thd_countdown.start()

        # The process is running
        # User wants to STOP the process
        else :
            run = False
            self.img_led.setEnabled(False)
            self.button_run_stop.setText("RUN")
            displayed = 0
            self.label_info_timer.setText(f"{'00:00'} \n\nDisplayed : {displayed}" )

            self.frame_browse.setEnabled(True)

    def browse(self):
        """ 'Browse...' button behaviour.
        OS opens window allowing the user to choose a directory 
        containing images. """

        global directory

        fname = QFileDialog()
        fname.setFileMode(QFileDialog.Directory) # Directory mode
        fname.setOption(QFileDialog.ShowDirsOnly, True)
        directory = fname.getExistingDirectory() # Get the choosen dir
        directory = os.path.normpath(directory) # Standardize syntax

        # The chosen folder must contain at least two images 
        # to unlock the next step and thus being able 
        # to start the process
        if self.imgCount() <= 1:
            self.label_status.setText("Not enough images in the selected directory")
            self.frame_timer.setEnabled(False)
            self.button_run_stop.setEnabled(False)

            self.label_info_browse.setText(
            f"Path : {directory}\n\nImages found = {self.imgCount()}")

            return None

        else :
            self.label_status.setText("")

        self.label_info_browse.setText(
            f"Path : {directory}\n\nImages found = {self.imgCount()}")
        
        self.frame_timer.setEnabled(True)
        self.button_run_stop.setEnabled(True)
    
    def imgCount(self):
        """Counts the number of images in the directory chosen 
        by the user"""

        global directory

        imgs = len([f for f in os.listdir(directory)
        if f.endswith('.jpg')
        or f.endswith('jpeg')
        or f.endswith('png')
        and os.path.isfile(os.path.join(directory, f))])

        return imgs # Number of images <int>
    
    def countdown(self):
        """Countdown set by the user to periodically 
        change the wallpaper. 
        This function is started in a thread"""

        global directory, displayed, run

        t_init = int(self.timer_box.text())
        t = t_init
        unit = self.comboBox_unit.currentText()

        if unit == "Min.":
            t = t * 60

        while run:
            while t and run == True:
                mins, secs = divmod(t, 60)
                timer = 'Next wallpaper in : {:02d}:{:02d}'.format(mins, secs)
                self.label_info_timer.setText(f"{timer} \n\nDisplayed : {displayed}" )
                time.sleep(1)
                t -= 1
            if run:
                self.wallpaperize(directory) # Change the wallpaper

            # Countdown reset
            if unit == "Min.":
                t = t_init * 60
            else:
                t = t_init

    def wallpaperize(self, path):
        """Randomly choose an image from the directory 
        chosen by the user and set it as wallpaper"""

        global displayed, run
        i = 0

        while True:
            x = random.choice(os.listdir(path))
            # print(x)

            # After a certain number of attempts without 
            # finding an image, the process stops
            if i > 50:
                run = False
                self.label_status.setText("Not enough images in the selected directory")
                self.button_run_stop.setText("RUN")
                self.img_led.setEnabled(True)
                return None

            # Extensions sought
            if x.endswith(".jpg") or x.endswith(".jpeg") or x.endswith(".png"):
                break
            
            # Not an image, try again
            else:
                i+=1
                print("Not an image")
                continue
        
        # Image found
        path = os.path.join(path, x)
        set_wallpaper(path)
        displayed += 1
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())