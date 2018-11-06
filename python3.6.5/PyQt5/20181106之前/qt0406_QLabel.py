# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWin02.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
from PyQt5.QtWidgets import QApplication,QLabel,QWidget,QVBoxLayout
# from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap,QPalette
import sys

class WindowDemo(QWidget):
	def __init__(self):
		super().__init__()
		
		label1 = QLabel(self)
		label2 = QLabel(self)
		label3 = QLabel(self)
		label4 = QLabel(self)
		# label2 = QLabel(self)
		#1 初始化标签控件
		
		label1.setText("这是一个文本标签")
		
		label1.setAutoFillBackground(True)
		palette = QPalette()
		palette.setColor(QPalette.Window,Qt.blue)
		label1.setPalette(palette)
		label1.setAlignment(Qt.AlignCenter)
		
		label2.setText("<a href='#'>欢迎使用Python GUI 应用</a>")
		
		label3.setToolTip('这是一个图片标签')
		label3.setPixmap(QPixmap("./images/python.jpg"))
		
		label4.setText("<a href='http://www.cnblogs.com/wangshuo1/'>欢迎访问信平的小屋</a>")
		
		label4.setAlignment(Qt.AlignRight)
		label4.setToolTip('这是一个超链接标签')
		
		#2在窗口 布局中添加控件
		vbox = QVBoxLayout()
		vbox.addWidget(label1)
		vbox.addStretch()
		vbox.addWidget(label2)
		vbox.addStretch()
		vbox.addWidget(label3)
		vbox.addStretch()
		vbox.addWidget(label4)
		
		#3 允许label控件访问超链接
		label1.setOpenExternalLinks(True)
		#打开允许超链接，默认是不允许，需要使用setOpenExternalLinks(True)允许浏览器访问超链接
		label4.setOpenExternalLinks(True)
		#点击文本框绑定槽事件
		label4.linkActivated.connect(self.link_clicked)
		
		#滑过文本框绑定槽事件
		label2.linkHovered.connect(self.link_hovered)
		label1.setTextInteractionFlags(Qt.TextSelectableByMouse)
		
		self.setLayout(vbox)
		self.setWindowTitle("QLabel1例子")
	def link_hovered():
		print("当鼠标滑过label2标签时触发事件")
	def link_clicked():
		print("当用鼠标点击label4标签是触发事件")
if __name__ == "__main__":
	app = QApplication(sys.argv)
	win = WindowDemo()
	win.show()
	sys.exit(app.exec())
		
		
		