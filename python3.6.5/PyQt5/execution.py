# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\SVN\Code\Python\trunk\Project\firstMainWin.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

#from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QFileDialog
from selectDisplay import Ui_MainWindow

class Ui(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        super(QMainWindow, self).__init__()
        self.setupUi(self)
        print(dir(self))
        #菜单点击关闭时，连接槽函数close()
        self.Close.triggered.connect(self.close)
        self.Open.triggered.connect(self.openMsg)
    def openMsg(self):
        file, ok = QFileDialog.getOpenFileName(self, "打开", "F:/", "ALL dffsfs Files (*);;Text Files (*.txt)")
        self.statusbar.showMessage(file)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ui = Ui()
    ui.show()
    sys.exit(app.exec_())

