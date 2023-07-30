#! /bin/python

### 导入必要库
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5 import uic
import os

class mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=uic.loadUi("main.ui")  #导入ui文件
        self.ui.show()

        self.ui.Button_print.clicked.connect(self.button_0)  ## 点击 Button_print 事件
        self.ui.Clear_Button.clicked.connect(self.button_clear)   ## Clear_Button 事件  （清理输出）
        
    def button_0 (self):
        strz=self.ui.textEdit_0.toPlainText()   ### 给 strz 赋值 textEdit_0 内的内容
        print(strz)  ## 打印 strz
        self.ui.textEdit_0.setText("")  #清理 textEdit_0 内容

    def button_clear(self):  
        os.system("clear")##调用 clear

# 显示
if __name__ == "__main__":
    app=QApplication(sys.argv)
    window=mainwindow()
    sys.exit(app.exec_())    
