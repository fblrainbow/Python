#!/usr/bin/env python
#coding:utf-8
import pymysql
import sys
from PyQt5.QtWidgets import *
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

class Table(QWidget):
    def __init__(self,data):
        super(Table,self).__init__()
        self.setWindowTitle("CSDN")
        self.resize(500,300);
        self.model = QStandardItemModel(len(data),len(data[0]));
        self.model.setHorizontalHeaderLabels(['博客名','原创','粉丝','浏览次数','排名','时间'])
        for index,tupleData in enumerate(list(data)):
            for column,content in enumerate(list(tupleData)):
                item = QStandardItem("%s"%(content))
                self.model.setItem(index,column,item)
        self.tableView = QTableView();
        self.tableView.setModel(self.model)
        dlgLayout = QVBoxLayout();
        dlgLayout.addWidget(self.tableView)
        self.setLayout(dlgLayout)

if __name__ == "__main__":
    url = "https://me.csdn.net/qq_37608398"   #总网站
    dataRerd = dataDeal("select * from csdn;")
    print(dataDeal("desc csdn;"))
    app = QApplication(sys.argv)
    table = Table(dataRerd)
    table.show()
    sys.exit(app.exec_())