#!/usr/bin/env python
#coding:utf-8
import pymysql
import sys
from PyQt5.QtWidgets import QApplication,QWidget,QFormLayout,QVBoxLayout,QListView,QMessageBox
from PyQt5.QtGui import *
from PyQt5.QtCore import *

def dataDeal(content):
    db = pymysql.connect(host = 'localhost',user = 'root',passwd ='FBLATPX520@',db = 'csdn',charset='utf8' )
    cursor = db.cursor()
    cursor.execute(content)
    ret = cursor.fetchall()
    db.commit()
    db.close()
    return  ret

def Table(QWidget):
    def __init__(self,parent = None):
        super(Table,self).__init__(parent)
        self.setWindowTitle("CSDN")
        self.resize(500,300);
        self.model = QStandardItemModel(4,4);
        self.model.setHorizontalHeaderLabels(['博客名','原创','粉丝','浏览次数','排名','时间'])
        for row in range(3):
            for column in range(6):
                item = QStandardItem("%s,%s"%(row,column))
                self.model.setItem(row,column,item)
        self.tableView = QTableView();
        self.tableView.setModel(self.model)
        dlgLayout = QVBoxLayout();
        dlgLayout.addWidget(self.tableView)
        self.setLayout(dlgLayout)

if __name__ == "__main__":
    # url = "https://me.csdn.net/qq_37608398"   #总网站
    # dataRerd = dataDeal("select * from csdn;")
    # print(dataRerd)
    # print(len(dataRerd))
    app = QApplication(sys.argv)
    table = Table()
    table.show()
    sys.exit(app.exec_())