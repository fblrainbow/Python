from PyQt5.QtWidgets import QApplication,QLineEdit,QWidget,QFormLayout
from PyQt5.QtGui import QIntValidator ,QDoubleValidator,QFont
from PyQt5.QtCore import Qt 
import sys

class lineEditDemo(QWidget):
	def __init__(self,parent = None):
		super(lineEditDemo,self).__init__(parent)
		flo = QFormLayout()
		l1 = QLineEdit()
		self.l1 = l1
		flo.addRow("Display",l1)
		e1 = QLineEdit()
		e1.setEchoMode(QLineEdit.Password)
		flo.addRow("Password",e1)
		e1.editingFinished.connect(self.enterPress)
		self.e1 = e1
		self.setLayout(flo)
		self.setWindowTitle("QLineEdit例子")
		
	def enterPress(self):
		tmp = self.e1.text()
		self.l1.setText(tmp)
		print(tmp)
if __name__ == "__main__":
	app = QApplication(sys.argv)
	win = lineEditDemo()
	win.show()
	sys.exit(app.exec())