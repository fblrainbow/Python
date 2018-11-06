from PyQt5.QtWidgets import QApplication,QLineEdit,QWidget,QFormLayout
import sys

class lineEditDemo(QWidget):
	def __init__(self,parent = None):
		super(lineEditDemo,self).__init__(parent)
		self.setWindowTitle("QLineEdit例子")
		
		flo = QFormLayout()
		pNormalLineEdit = QLineEdit()
		pNoEchoLineEdit = QLineEdit()
		pPasswordLineEdit = QLineEdit()
		pPasswordEchoOnEditLineEdit = QLineEdit()
		
		flo.addRow("Normal",pNormalLineEdit)
		flo.addRow("NoEcho",pNoEchoLineEdit)
		flo.addRow("Password",pPasswordLineEdit)
		flo.addRow("PasswordEchoOnEdit",pPasswordEchoOnEditLineEdit)
		
		pNormalLineEdit.setPlaceholderText("Normal")
		pNoEchoLineEdit.setPlaceholderText("NoEcho")
		pPasswordLineEdit.setPlaceholderText("Password")
		pPasswordEchoOnEditLineEdit.setPlaceholderText("PasswordEchoOnEdit")
		
		self.setLayout(flo)
		
if __name__ == "__main__":
	app = QApplication(sys.argv)
	lineEditDemo1 = lineEditDemo()
	lineEditDemo1.show()
	sys.exit(app.exec())