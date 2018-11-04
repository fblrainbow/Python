# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\SVN\Code\Python\trunk\Project\firstMainWin.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

#from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QFileDialog
from MainForm2 import Ui_MainWindow
from MainWin02 import Ui_Form

class Ui(QMainWindow, Ui_Form):
    def __init__(self):
        super(Ui, self).__init__()
        super(QMainWindow, self).__init__()
        self.setupUi(self)
        
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ui = Ui()
    ui.show()
    sys.exit(app.exec_())

