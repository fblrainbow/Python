import sys
from PyQt5.QtWidgets import QWidget,QToolTip,QApplication
from PyQt5.QtGui import QFont

class WinForm(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()
		
	def initUI(self):
		QToolTip.setFont(QFont('SansSerif',10))
		self.setToolTip('这是一个<i><b>气泡提示</b></i>')
		self.setGeometry(200,300,400,400)
		self.setWindowTitle('气泡提示demo')
if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = WinForm()
	window.show()
	sys.exit(app.exec())