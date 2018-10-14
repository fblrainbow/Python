# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\SVN\Code\Python\trunk\Project\firstMainWin.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

#from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QApplication
from UI import Ui_MainWindow

class Ui(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(Ui_MainWindow, self).__init__()
        #self.setupUi(self)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

