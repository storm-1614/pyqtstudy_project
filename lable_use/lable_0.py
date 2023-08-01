#! /bin/python

import sys
from PyQt5.QtWidgets import QApplication,QWidget,QLabel

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w=QWidget()

    # # 下面创建一个 Label，然后调用方法指定父类
    w.setWindowTitle("lable_0")
    lable=QLabel("账号：",w)
    # 设置父对象
    lable.setParent(w)
    # 显示窗口位置与大小L：x, y, w, h
    lable.setGeometry(20,20,40,40)

    # 展示窗口
    w.show()

    # 程序进行循环等待状态
    app.exec_()
