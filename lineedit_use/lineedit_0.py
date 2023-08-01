#! /bin/python

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit

# 点击按钮后输出账号
def click():
    # 文本框内容赋值 text
    text = edit.text()
    print("账号:",text)

if __name__ == "__main__":
    app = QApplication (sys.argv)

    w = QWidget ()
    w.setWindowTitle("lineedit_0")

    # 纯文本
    lable = QLabel ("账号:",w)
    lable.setGeometry (20, 20, 40, 20)

    # 文本框
    edit = QLineEdit (w)
    edit.setPlaceholderText ("请输入账号")
    edit.setGeometry (75, 20, 200, 20)
    
    # 在窗口里面添加控件
    btn = QPushButton("注册",w)
    btn.setGeometry(50, 80, 70, 30)
    # 控件点击事件
    btn.clicked.connect(click)

    # 展示窗口
    w.show()

    #程序进行循环等待状态
    app.exec_()


