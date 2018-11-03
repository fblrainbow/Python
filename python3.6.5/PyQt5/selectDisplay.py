# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'selectDisplay.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(465, 445)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.selectDis = QtWidgets.QCheckBox(self.centralwidget)
        self.selectDis.setGeometry(QtCore.QRect(160, 110, 71, 16))
        self.selectDis.setObjectName("selectDis")
        self.dis1 = QtWidgets.QLabel(self.centralwidget)
        self.dis1.setGeometry(QtCore.QRect(120, 190, 54, 12))
        self.dis1.setObjectName("dis1")
        self.dis2 = QtWidgets.QLineEdit(self.centralwidget)
        self.dis2.setGeometry(QtCore.QRect(180, 190, 113, 20))
        self.dis2.setObjectName("dis2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 465, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.selectDis.clicked['bool'].connect(self.dis1.hide)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.selectDis.setText(_translate("MainWindow", "选择"))
        self.dis1.setText(_translate("MainWindow", "显示1"))
        self.dis2.setText(_translate("MainWindow", "显示2"))

