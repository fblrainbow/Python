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

class MyWindow(QWidget):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.workList = openWorkBook("csj.xlsx")
        #self.setLayout(layout)
        self.setWindowTitle("种群数据搜索")
        self.resize(700,200)
        #全局控件，用于“承载”全局变量
        #wwg = QWidget(self)
        #全局布局（注意参数wwg）
        self.gWg = QVBoxLayout(self)
        self.hlayout_Search = QHBoxLayout(self)
        self.hlayout_table = QHBoxLayout(self)
        
        
        #为局部布局添加控件
        self.hlayout_Search.addWidget(QLabel('种群'),0,Qt.AlignCenter)
        self.qle = QLineEdit(self)
        self.qle.setMaximumWidth(40)
        self.hlayout_Search.addWidget(self.qle,0,Qt.AlignLeft)
        self.search = QPushButton('搜索')
        self.search.setMaximumWidth(40)
        self.hlayout_Search.addWidget(self.search,1,Qt.AlignLeft)
        self.search.clicked.connect(self.getSearchText)
        self.tmodel = QStandardItemModel(3,18)
        self.tmodel.setHorizontalHeaderLabels(['种群','穗分枝数(个)','分支籽粒充实度(%)','a','b','R2','GR50(g a.i.ha-1)','95%置信区间(GR50)','IR','a','b','R2','GR50(g a.i.ha-1)','95%置信区间(GR50)','IR','采样地点','生境'])
        #self.tmodel.setHorizontalHeaderLabels(
        
        #['种群','穗分枝数(个)','分支籽粒充实度(%)','a','b','R2','GR50(g a.i.ha-1)','95%置信区间(GR50)','IR','a','b','R2','GR50(g a.i.ha-1)','95%置信区间(GR50)','IR','采样地点','生境'])
        self.tableView = QTableView(self)
        self.tableView.setModel(self.tmodel)
        self.tableView.setShowGrid(True)
        self.hlayout_table.addWidget(self.tableView)

        self.hwg_s = QWidget(self)
        self.hwg_t = QWidget(self)
        
        self.hwg_s.setLayout(self.hlayout_Search)
        self.hwg_t.setLayout(self.hlayout_table)
        
        
        self.gWg.addWidget(self.hwg_s)
        self.gWg.addWidget(self.hwg_t)
        self.setLayout(self.gWg)
    def getSearchText(self):
        #print(self.qle.text())
        self.searchText = self.qle.text()
        self.retList = searchData(self.searchText,self.workList)
        #print(self.retList)
        if len(self.retList) == 0:
            print("没有搜索到该种群")
            return
        tableList = [self.retList[0][0],self.retList[2][1],self.retList[2][2],self.retList[0][1],self.retList[0][2],self.retList[0][3],self.retList[0][4],self.retList[0][5],self.retList[0][6],self.retList[1][1],self.retList[1][2],self.retList[1][3],self.retList[1][4],self.retList[1][5],self.retList[1][6],self.retList[3][1],self.retList[3][2]]
        
        #print(tableList)
        print(dir(self.tmodel))
        self.tmodel.clear()
        for index,line in enumerate(tableList):
            item = QStandardItem(line)
            self.tmodel.setItem(2,index,item)
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
        self.addLayout(dlgLayout)
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
    demo = MyWindow()
    demo.show()
    sys.exit(app.exec_())


