#! /bin/python

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.uic import loadUi

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        loadUi("main.ui",self)
        
        self.currentPath = None

        self.actionnewFile.triggered.connect(self.newFile)
        self.actionsaveFile.triggered.connect(self.saveFile)
        self.actionSaveFileAs.triggered.connect(self.saveFileAs)
        self.actionopenFile.triggered.connect(self.openFile)
        self.actionundo.triggered.connect(self.undo)
        self.actionredo.triggered.connect(self.redo)
        self.actioncopy.triggered.connect(self.copy)
        self.actionpaste.triggered.connect(self.paste)
        

    def newFile(self):
        self.textEdit.clear()
        self.setWindowTitle("Untitled")
        self.currentPath = None
        
    
    def saveFile(self):
        if self.currentPath is not None:
            fileText = self.textEdit.toPlainText()
            with open(self.currentPath, 'w') as file:
                file.write(fileText)
        else:
            self.saveFileAs()
            
    def saveFileAs(self):
        pathName = QFileDialog.getSaveFileName(self,'Save file', '.', 'Text files(*.txt)')
        fileText = self.textEdit.toPlainText()
        if pathName[0] is not'':
            with open(pathName[0], 'w') as file:
                file.write(fileText)

            self.setWindowTitle(pathName[0])
            self.currentPath = pathName[0]
    
    def openFile(self):
        fileName = QFileDialog.getOpenFileName(self,'Open file', '.', 'Text files(*.txt)')
        self.setWindowTitle(fileName[0])
        if fileName[0] is not '':   
            with open(fileName[0], 'r') as file:
                fileText = file.read()
                self.textEdit.setText(fileText)
            self.currentPath = fileName[0]
    
    def undo(self):
        self.textEdit.undo()

    def redo(self):
        self.textEdit.redo()

    def copy(self):
        self.textEdit.copy()

    def paste(self):
        self.textEdit.paste()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    app.exec()
