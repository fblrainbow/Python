#coding:utf-8
import os
import sys
import xlrd
import xlwt
from xlutils.copy import copy
from datetime import datetime
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class InputdialogDemo(QWidget):
    def __init__(self, parent=None):
        super(InputdialogDemo, self).__init__(parent)
        self.workList = openWorkBook("csj.xlsx")
        layout = QFormLayout()
        self.btn2 = QPushButton("搜索种群")
        self.le2 = QLineEdit()
        self.btn2.clicked.connect(self.getIext)
        layout.addRow(self.btn2,self.le2)
        self.setLayout(layout)
        self.setWindowTitle("种群数据搜索")
        self.resize(300,150)
    def getIext(self):
        text = self.le2.text()
        self.retList = searchData(text,self.workList)
        print(self.retList)
        self.model = QStandardItemModel(1,17);
        self.model.setHorizontalHeaderLabels(['种群','穗分枝数(个)','分支籽粒充实度(%)','a','b','R2','GR50(g a.i.ha-1)','95%置信区间(GR50)','IR','a','b','R2','GR50(g a.i.ha-1)','95%置信区间(GR50)','IR','采样地点','生境'])
        item = QStandardItem('0')
        self.model.setItem(0,0,item)
        self.tableView = QTableView()
        self.tableView.setModel(self.model)
        dlgLayout = QVBoxLayout();
        dlgLayout.addWidget(self.tableView)
        self.setLayout(dlgLayout)
def openWorkBook(fileName):
    workbook = xlrd.open_workbook(fileName)
    sheetName_0 = workbook.sheet_by_name("不同种群牛筋草对百草枯的抗药性水平")
    sheetName_1 = workbook.sheet_by_name("不同种群牛筋草对草甘膦的抗药性水平")
    sheetName_2 = workbook.sheet_by_name("不同种群牛筋草对草铵膦的抗药性水平")
    sheetName_3 = workbook.sheet_by_name("不同种群牛筋草穗部形态指标调查")
    sheetName_4 = workbook.sheet_by_name("不同种群牛筋草种植采集地点及用药史")
    table_all = []
    table_all.append(sheetName_0)
    table_all.append(sheetName_1)
    table_all.append(sheetName_2)
    table_all.append(sheetName_3)
    table_all.append(sheetName_4)
    workList = []
    for i in table_all:
        tmpTable = i
        rowList = []
        for j in range(0,tmpTable.nrows,1):
            colList = []
            for k in range(0,tmpTable.ncols,1):
                colList.append(str(tmpTable.cell(j,k).value).replace("\xa0","").replace("\n",""))
            rowList.append(colList)
        workList.append(rowList)
    return workList
        
def searchData(string,objTable):
    objDataList = []
    for index,singleTable in enumerate(objTable):
        for line in singleTable[1:]:
            if line[0] == string:
                objDataList.append(line)
    return objDataList

if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = InputdialogDemo()
    demo.show()
    sys.exit(app.exec_())


