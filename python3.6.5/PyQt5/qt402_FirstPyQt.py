#coding:utf-8
import sys
from PyQt5.QtWidgets import QApplication,QWidget

app = QApplication(sys.argv)
window = QWidget()
window.resize(300,200)
window.move(300,500)
window.setWindowTitle('Hello PyQt5')
window.show()
sys.exit(app.exec())