#! /bin/python

### 导入必要库
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5 import uic

class mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=uic.loadUi("main.ui")  #导入ui文件
        self.ui.show()
        
        self.ui.pushButton_0.clicked.connect(self.clickButton_0)   ## 第一个按钮功能
        self.ui.pushButton_1.clicked.connect(self.clickButton_1)
    
    def clickButton_0(self):   ##定义第一个按钮功能
        print("点击第一个按钮")
    
    def clickButton_1(self):
        sender = self.sender()   ## self.sender() 指发送信号的对象
        print(sender.text(),'被点击')    # sender.text() 获取点击对象名字


# 显示
if __name__ == "__main__":
    app=QApplication(sys.argv)
    window=mainwindow()
    sys.exit(app.exec_())
