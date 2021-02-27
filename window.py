from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.setWindowTitle("Wallpaper changer")
        mainWindow.setEnabled(True)
        mainWindow.resize(800, 500)
        mainWindow.setMinimumSize(QtCore.QSize(800, 500))
        mainWindow.setMaximumSize(QtCore.QSize(800, 500))

        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Label title
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(20, 10, 311, 61))
        self.label_title.setText("WALLPAPER CHANGER")
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_title.setFont(font)

        # Line
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(-10, 50, 341, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)

        # Frame browse
        self.frame_browse = QtWidgets.QFrame(self.centralwidget)
        self.frame_browse.setEnabled(True)
        self.frame_browse.setGeometry(QtCore.QRect(10, 110, 291, 341))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.frame_browse.setFont(font)
        self.frame_browse.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_browse.setFrameShadow(QtWidgets.QFrame.Plain)

        # label step 1
        self.label_step_1 = QtWidgets.QLabel(self.frame_browse)
        self.label_step_1.setGeometry(QtCore.QRect(50, 0, 201, 51))
        self.label_step_1.setText("Step 1 : Choose the folder")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_step_1.setFont(font)

        # Button browse
        self.button_browse = QtWidgets.QPushButton(self.frame_browse)
        self.button_browse.setGeometry(QtCore.QRect(70, 130, 141, 41))
        self.button_browse.setText("Browse...")
        self.button_browse.setDefault(False)
        self.button_browse.setFlat(False)

        # Frame info browse
        self.frame_info_browse = QtWidgets.QFrame(self.frame_browse)
        self.frame_info_browse.setGeometry(QtCore.QRect(10, 220, 271, 111))
        self.frame_info_browse.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_info_browse.setFrameShadow(QtWidgets.QFrame.Raised)

        # Label info browse
        self.label_info_browse = QtWidgets.QLabel(self.frame_info_browse)
        self.label_info_browse.setGeometry(QtCore.QRect(10, 10, 251, 91))
        self.label_info_browse.setWordWrap(True)
        self.label_info_browse.setText("Path : ...\n\n"+
        "Images found : ...")
        self.label_info_browse.setAlignment(QtCore.Qt.AlignCenter)

        # Frame timer
        self.frame_timer = QtWidgets.QFrame(self.centralwidget)
        self.frame_timer.setEnabled(True)
        self.frame_timer.setGeometry(QtCore.QRect(330, 110, 291, 341))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.frame_timer.setFont(font)
        self.frame_timer.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_timer.setFrameShadow(QtWidgets.QFrame.Plain)

        # Label step 2
        self.label_step_2 = QtWidgets.QLabel(self.frame_timer)
        self.label_step_2.setGeometry(QtCore.QRect(50, 0, 201, 51))
        self.label_step_2.setText("Step 2 : Choose a timer")
        font.setPointSize(12)
        self.label_step_2.setFont(font)

        # Timer box
        self.timer_box = QtWidgets.QSpinBox(self.frame_timer)
        self.timer_box.setGeometry(QtCore.QRect(100, 130, 71, 41))
        self.timer_box.setMinimum(1)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.timer_box.setFont(font)
        self.timer_box.setAlignment(QtCore.Qt.AlignCenter)

        # Label every
        self.label_every = QtWidgets.QLabel(self.frame_timer)
        self.label_every.setGeometry(QtCore.QRect(42, 134, 51, 31))
        self.label_every.setText("Every :")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_every.setFont(font)

        # Combobox unit
        self.comboBox_unit = QtWidgets.QComboBox(self.frame_timer)
        self.comboBox_unit.setGeometry(QtCore.QRect(190, 130, 69, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.comboBox_unit.setFont(font)
        self.comboBox_unit.addItems(["Min.", "Sec."])

        # Frame info timer
        self.frame_info_timer = QtWidgets.QFrame(self.frame_timer)
        self.frame_info_timer.setGeometry(QtCore.QRect(10, 220, 271, 111))
        self.frame_info_timer.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_info_timer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_info_timer.setObjectName("frame_info_timer")

        # Label info timer
        self.label_info_timer = QtWidgets.QLabel(self.frame_info_timer)
        self.label_info_timer.setText("Next wallpaper in : 00:02:32\n\n"+
        "Displayed : 4")
        self.label_info_timer.setGeometry(QtCore.QRect(10, 10, 251, 91))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_info_timer.setFont(font)
        self.label_info_timer.setAlignment(QtCore.Qt.AlignCenter)

        # Button RUN/STOP
        self.button_run_stop = QtWidgets.QPushButton(self.centralwidget)
        self.button_run_stop.setGeometry(QtCore.QRect(670, 230, 111, 61))
        self.button_run_stop.setText("RUN")
        font = QtGui.QFont()
        font.setPointSize(15)
        self.button_run_stop.setFont(font)

        # Image logo
        self.img_logo = QtWidgets.QLabel(self.centralwidget)
        self.img_logo.setGeometry(QtCore.QRect(679, 0, 111, 100))
        self.img_logo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.img_logo.setFrameShadow(QtWidgets.QFrame.Sunken)
        #self.img_logo.setText("Not found")
        self.img_logo.setPixmap(QtGui.QPixmap("./files/logo.png"))
        self.img_logo.setScaledContents(True)

        # Label status
        self.label_status = QtWidgets.QLabel(self.centralwidget)
        self.label_status.setGeometry(QtCore.QRect(10, 470, 781, 21))
        self.label_status.setText("")
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_status.setFont(font)
        self.label_status.setAlignment(QtCore.Qt.AlignCenter)

        # Image LED
        self.img_led = QtWidgets.QLabel(self.centralwidget)
        self.img_led.setEnabled(True)
        self.img_led.setGeometry(QtCore.QRect(632, 247, 30, 30))
        self.img_led.setPixmap(QtGui.QPixmap("./files/led_green.png"))
        self.img_led.setScaledContents(True)

        mainWindow.setCentralWidget(self.centralwidget)

        QtCore.QMetaObject.connectSlotsByName(mainWindow)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())