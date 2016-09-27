#!/usr/bin/env python
"""
Rename all files inside specified folder.
"""

# Python stuff
import sys
import os
import posixpath

# QT stuff
from PySide.QtGui import QDialog, QMainWindow, QPushButton, QApplication
from PySide import QtCore
from batch_rename_ui import Ui_Dialog

class MainWindow(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.progressBar.reset()
        # TODO : Font size of search and replace text

        self.btn_rename.released.connect(self.renameButtonPressed)

    def renameButtonPressed(self):
        inpPath = self.inp_path.text()
        oldText = self.inp_oldText.text()
        newText = self.inp_newText.text()

        # Check Source Folder
        if not os.path.exists(inpPath):
            print "Source Folder not found."
            return
        if os.path.isfile(inpPath):
            print "Source Folder can't be a file."
            return

        # Check oldText
        if oldText == "":
            print "Write some text to replace."

        # Check newNext
        if newText == "":
            print "Write some new text to insert."

        self.batchRename(inpPath,oldText,newText)

    def batchRename(self,path,oldName,newName):
        if not os.path.exists(path):
            print "Invalid path"
            return

        files = os.listdir(path)
        failedFiles = 0
        for file in files:
            newFileName = file.replace(oldName,newName)
            oldFile = os.path.join(path,file)
            newFile = os.path.join(path,newFileName)
            print "Renaming : %s  to  %s"%(file,newFileName)
            try:
                os.rename(oldFile,newFile)
                pass
            except:
                failedFiles+=1
        if failedFiles>0:
            print "Renaming failed on %s files"%(failedFiles)
        print "Batch Rename : Done"

if __name__ == '__main__':
    app = QApplication(sys.argv)
    frame = MainWindow()
    frame.show()
    app.exec_()