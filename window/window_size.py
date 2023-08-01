#! /bin/python

import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    w = QWidget()

    w.setWindowTitle("Window_Size")
    
    # 窗口的大小 x,y
    w.resize(300, 300)

    w.show()

    app.exec()

