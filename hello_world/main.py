#! /bin/python

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic

class mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=uic.loadUi("main.ui")
        #PushButton Button 是在ui内
        self.ui.Button.clicked.connect(self.clickButton)
        self.ui.show()


    def clickButton(self):
        sender = self.sender()  # 对象名
        print(sender.text()+'被点击')

if __name__=="__main__":
    app=QApplication(sys.argv)
    window=mainwindow()
    sys.exit(app.exec_())
