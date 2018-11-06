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
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 465, 23))
        self.menubar.setObjectName("menubar")
        self.menu_F = QtWidgets.QMenu(self.menubar)
        self.menu_F.setObjectName("menu_F")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.Open = QtWidgets.QAction(MainWindow)
        self.Open.setChecked(False)
        self.Open.setVisible(True)
        self.Open.setObjectName("Open")
        self.New = QtWidgets.QAction(MainWindow)
        self.New.setObjectName("New")
        self.Close = QtWidgets.QAction(MainWindow)
        self.Close.setObjectName("Close")
        self.actionedit = QtWidgets.QAction(MainWindow)
        self.actionedit.setObjectName("actionedit")
        self.addWinAction = QtWidgets.QAction(MainWindow)
        self.addWinAction.setObjectName("addWinAction")
        self.menu_F.addAction(self.Open)
        self.menu_F.addAction(self.New)
        self.menu_F.addAction(self.Close)
        self.menu.addAction(self.actionedit)
        self.menubar.addAction(self.menu_F.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.toolBar.addAction(self.addWinAction)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menu_F.setTitle(_translate("MainWindow", "文件(&F)"))
        self.menu.setTitle(_translate("MainWindow", "编辑(&E)"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.Open.setText(_translate("MainWindow", "打开"))
        self.Open.setToolTip(_translate("MainWindow", "<html><head/><body><p><a href=\"https://www.baidu.com\"><span style=\" text-decoration: underline; color:#0000ff;\">打开</span></a></p></body></html>"))
        self.Open.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.New.setText(_translate("MainWindow", "新建"))
        self.New.setToolTip(_translate("MainWindow", "新建"))
        self.New.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.Close.setText(_translate("MainWindow", "关闭"))
        self.Close.setToolTip(_translate("MainWindow", "关闭"))
        self.Close.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.actionedit.setText(_translate("MainWindow", "edit"))
        self.addWinAction.setText(_translate("MainWindow", "添加窗体"))
        self.addWinAction.setToolTip(_translate("MainWindow", "添加窗体"))

