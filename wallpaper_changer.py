import sys
import os
import random
import threading
import time

from wallpaper import set_wallpaper
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QFileDialog

from window import Ui_mainWindow

directory = ""
displayed = 0
run = False

class MainWindow(QtWidgets.QMainWindow, Ui_mainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.frame_timer.setEnabled(False)
        self.button_run_stop.setEnabled(False)

        self.button_run_stop.clicked.connect(self.run_button)
        self.button_browse.clicked.connect(self.browse)
        self.img_led.setEnabled(False)

    def run_button(self):
        global run, displayed

        if (self.button_run_stop.text() == "RUN"):
            run = True
            self.img_led.setEnabled(True)
            self.button_run_stop.setText("STOP")
            self.label_status.setText("")

            self.frame_browse.setEnabled(False)

            thd_countdown = threading.Thread(target=self.countdown)
            thd_countdown.start()

        else :
            run = False
            self.img_led.setEnabled(False)
            self.button_run_stop.setText("RUN")
            displayed = 0
            self.label_info_timer.setText(f"{'00:00'} \n\nDisplayed : {displayed}" )

            self.frame_browse.setEnabled(True)

    def browse(self):
        global directory

        fname = QFileDialog()
        fname.setFileMode(QFileDialog.Directory)
        fname.setOption(QFileDialog.ShowDirsOnly, True)
        directory = fname.getExistingDirectory() # Get the choosen dir
        directory = os.path.normpath(directory)

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
        global directory

        imgs = len([f for f in os.listdir(directory)
        if f.endswith('.jpg')
        or f.endswith('jpeg')
        or f.endswith('png')
        and os.path.isfile(os.path.join(directory, f))])

        return imgs
    
    def countdown(self):
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
                self.wallpaperize(directory)
            #print("FINISH")
            t = t_init


    def wallpaperize(self, path):
        global displayed, run
        i = 0

        while True:
            x = random.choice(os.listdir(path))
            # print(x)

            if i > 50:
                run = False
                self.label_status.setText("Not enough images in the selected directory")
                self.button_run_stop.setText("RUN")
                self.img_led.setEnabled(True)
                return None

            if x.endswith(".jpg") or x.endswith(".jpeg") or x.endswith(".png"):
                break

            else:
                i+=1
                print("Not an image")
                continue

        path = os.path.join(path, x)
        set_wallpaper(path)
        displayed += 1
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())