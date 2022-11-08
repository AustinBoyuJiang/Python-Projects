from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import tkinter
import sys


class WindowUi(QWidget):
    def __init__(self):
        super().__init__()
        screen = tkinter.Tk()
        self.screenWidth = screen.winfo_screenwidth()
        self.screenHeight = screen.winfo_screenheight()
        self.initWindow()
        self.initBackground()
        self.initText()
        self.showFullScreen()

    def initWindow(self):
        self.move(0, 0)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)

    def initBackground(self):
        self.background = QLabel(self)
        self.background.resize(self.screenWidth, self.screenHeight)
        self.background.setStyleSheet("background-color: #0078d9")

    def initText(self):
        self.text = QLabel(self)
        rate = self.screenWidth / 4000
        width = 1685 * rate
        height = 882 * rate
        x = (self.screenWidth - width) / 2
        y = (self.screenHeight - height) / 2 - self.screenHeight * 0.05
        self.text.resize(width, height)
        self.text.move(x, y)
        img = QPixmap("text.png")
        self.text.setPixmap(img)
        self.text.setScaledContents(True)

    def center(self):
        window = self.frameGeometry()
        center = QDesktopWidget().availableGeometry().center()
        window.moveCenter(center)
        return window.topLeft()

    def closeEvent(self, event):
        event.ignore()


if (__name__ == "__main__"):
    app = QApplication(sys.argv)
    loginWindow = WindowUi()
    app.exec_()
