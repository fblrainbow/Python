# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_closeWinBtn(object):
    def setupUi(self, closeWinBtn):
        closeWinBtn.setObjectName("closeWinBtn")
        closeWinBtn.resize(400, 300)
        self.pushButton = QtWidgets.QPushButton(closeWinBtn)
        self.pushButton.setGeometry(QtCore.QRect(140, 80, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(closeWinBtn)
        self.pushButton.clicked.connect(closeWinBtn.close)
        QtCore.QMetaObject.connectSlotsByName(closeWinBtn)

    def retranslateUi(self, closeWinBtn):
        _translate = QtCore.QCoreApplication.translate
        closeWinBtn.setWindowTitle(_translate("closeWinBtn", "Form"))
        self.pushButton.setText(_translate("closeWinBtn", "关闭窗口"))

