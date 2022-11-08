from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import *
import pyautogui
import ctypes
import socket
import _thread
import sys


class mainUi(QWidget):
    def __init__(self):
        super().__init__()
        self.dialog = ''
        self.flag = False
        self.initWindow()
        self.initTitleText()
        self.initCloseButton()
        self.initMinButton()
        self.initDialogBox()
        self.initEditArea()
        self.initEditText()
        self.initIpLabel()
        self.initIpEdit()
        self.initSendButton()
        self.initConfirmButton()
        self.show()


    def initWindow(self):
        width, height = 800, 630
        self.resize(width, height)
        self.move(self.center())
        self.windowX = self.x()
        self.windowY = self.y()
        self.setMinimumWidth(width)
        self.setMinimumHeight(height)
        self.setMaximumWidth(width)
        self.setMaximumHeight(height)
        self.setWindowTitle('Chat Room')
        self.setWindowOpacity(0.9)
        self.setStyleSheet("background-color: #ffffff;")
        self.setWindowIcon(QIcon("Chat Room Icon.ico"))
        self.setWindowFlags(Qt.FramelessWindowHint)

    def initTitleText(self):
        self.titleTxt = QLabel(self)
        self.titleTxt.resize(720, 30)
        self.titleTxt.move(0, 0)
        self.titleTxt.setText('  Chat Room')
        self.titleTxt.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.titleTxt.setStyleSheet("font-family: 'Arial';"
                                    "font-size: 15px;"
                                    "color: #ffffff;"
                                    "background-color: #272a2d;")

    def initCloseButton(self):
        self.closeButton = QPushButton(self)
        self.closeButton.setObjectName('closeButton')
        self.closeButton.setText('×')
        self.closeButton.resize(40, 30)
        self.closeButton.move(760, 0)
        self.closeButton.clicked.connect(self.close)
        self.closeButton.setToolTip('close')
        self.closeButton.setStyleSheet("QPushButton#closeButton{font-family: Arial;"
                                       "font-size: 20px;"
                                       "border: 0px;"
                                       "color: #ffffff;"
                                       "background-color: #272a2d;}"
                                       "QPushButton#closeButton:hover{background-color: #e81123;}"
                                       "QPushButton#closeButton:pressed{background-color: #9b0000;}")

    def initMinButton(self):
        self.minButton = QPushButton(self)
        self.minButton.setObjectName('minButton')
        self.minButton.setText('-')
        self.minButton.resize(40, 30)
        self.minButton.move(720, 0)
        self.minButton.clicked.connect(self.showMinimized)
        self.minButton.setToolTip('minimized')
        self.minButton.setStyleSheet("QPushButton#minButton{font-family: Arial;"
                                     "font-size: 20px;"
                                     "border: 0px;"
                                     "color: #ffffff;"
                                     "background-color: #272a2d;}"
                                     "QPushButton#minButton:hover{background-color: #464646;}"
                                     "QPushButton#minButton:pressed{background-color: #656565;}")

    def initDialogBox(self):
        self.dialogBox = QTextEdit(self)
        self.dialogBox.resize(760, 360)
        self.dialogBox.move(20, 50)
        self.dialogBox.setFocusPolicy(Qt.NoFocus)
        self.dialogBox.verticalScrollBar().hide()
        self.dialogBox.setStyleSheet("font-family: 'Microsoft YaHei UI';"
                                     "font-size: 18px;"
                                     "color: #000000;"
                                     "background-color: #ffffff;"
                                     "border: 0px;")

    def initEditArea(self):
        self.editText = QLabel(self)
        self.editText.resize(800, 200)
        self.editText.move(0, 430)
        self.editText.setStyleSheet("background-color: #f1f1f1;"
                                    "border: 0px;")

    def initEditText(self):
        self.editText = QTextEdit(self)
        self.editText.resize(760, 120)
        self.editText.move(20, 450)
        self.editText.verticalScrollBar().hide()
        self.editText.setStyleSheet("font-family: 'Microsoft YaHei UI';"
                                    "font-size: 18px;"
                                    "color: #000000;"
                                    "background-color: #f1f1f1;"
                                    "border: 0px;")

    def initIpLabel(self):
        self.ipLabel = QLabel(self)
        self.ipLabel.setText("  Server IP: ")
        self.ipLabel.resize(620, 30)
        self.ipLabel.move(20, 585)
        self.ipLabel.setStyleSheet("font-family: 'Microsoft YaHei UI';"
                                    "font-size: 18px;"
                                    "color: #000000;"
                                    "background-color: #f1f1f1;"
                                    "border: 0px;")

    def initIpEdit(self):
        self.ipEdit = QLineEdit(self)
        self.ipEdit.resize(520, 30)
        self.ipEdit.move(120, 585)
        self.ipEdit.setStyleSheet("font-family: 'Microsoft YaHei UI';"
                                  "font-size: 18px;"
                                  "color: #000000;"
                                  "background-color: #f1f1f1;"
                                  "border: 0px;")

    def initSendButton(self):
        self.sendButton = QPushButton(self)
        self.sendButton.setVisible(False)
        self.sendButton.setObjectName('sendButton')
        self.sendButton.setText('Send')
        self.sendButton.resize(100, 30)
        self.sendButton.move(670, 585)
        self.sendButton.clicked.connect(self.send)
        self.sendButton.setToolTip('Send the message')
        self.sendButton.setStyleSheet("QPushButton#sendButton{font-family: Arial;"
                                      "font-size: 18px;"
                                      "border: 0px;"
                                      "color: #000000;"
                                      "background-color: #d2d2d2;"
                                      "border-radius: 10px}"
                                      "QPushButton#sendButton:hover{background-color: #b2b2b2;}"
                                      "QPushButton#sendButton:pressed{background-color: #949494;}")

    def initConfirmButton(self):
        self.confirmButton = QPushButton(self)
        self.confirmButton.setObjectName('confirmButton')
        self.confirmButton.setText('Confirm')
        self.confirmButton.resize(100, 30)
        self.confirmButton.move(670, 585)
        self.confirmButton.clicked.connect(self.set_server)
        self.confirmButton.setToolTip('Confirm the server IP')
        self.confirmButton.setStyleSheet("QPushButton#confirmButton{font-family: Arial;"
                                         "font-size: 18px;"
                                         "border: 0px;"
                                         "color: #000000;"
                                         "background-color: #d2d2d2;"
                                         "border-radius: 10px}"
                                         "QPushButton#confirmButton:hover{background-color: #b2b2b2;}"
                                         "QPushButton#confirmButton:pressed{background-color: #949494;}")

    def center(self):
        window = self.frameGeometry()
        center = QDesktopWidget().availableGeometry().center()
        window.moveCenter(center)
        return window.topLeft()

    def mousePressEvent(self, event):
        self.startX, self.startY = pyautogui.position()
        if (event.windowPos().x() >= 0 and event.windowPos().x() <= 720):
            if (event.windowPos().y() >= 0 and event.windowPos().y() <= 30):
                self.flag = True

    def mouseReleaseEvent(self, event):
        self.windowX = self.x()
        self.windowY = self.y()
        self.flag = False

    def mouseMoveEvent(self, event):
        if (self.flag == True):
            moveX, moveY = pyautogui.position()
            nextX = self.windowX + moveX - self.startX
            nextY = self.windowY + moveY - self.startY
            self.move(nextX, nextY)

    def set_server(self):
        global server
        self.ipEdit.setFocusPolicy(Qt.NoFocus)
        self.sendButton.setVisible(True)
        self.confirmButton.setVisible(False)
        host = self.ipEdit.text()
        port = 9999
        server.connect((host, port))
        _thread.start_new_thread(get_msg, ())

    def send(self):
        print(1)
        msg = self.editText.toPlainText()
        msg = msg.replace('\n',' ')
        while(len(msg)>0 and (msg[-1]==' ' or msg[-1]=='\n')):
            msg = msg[:-1]
        if(msg!=''):
            self.editText.clear()
            server.send(msg.encode('utf-8'))


def get_msg():
    while (True):
        try:
            msg = server.recv(1024).decode('utf-8')
            window.dialogBox.insertPlainText(msg + "\n")
            cursor = window.dialogBox.textCursor()
            cursor.movePosition(QTextCursor.End)
            window.dialogBox.setTextCursor(cursor)
        except:
            break


if (__name__ == "__main__"):
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    app = QApplication(sys.argv)
    window = mainUi()
    sys.exit(app.exec_())
    server.close()
