import sys

from PyQt5 import QtWidgets, QtCore

from window import Ui_mainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_mainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())