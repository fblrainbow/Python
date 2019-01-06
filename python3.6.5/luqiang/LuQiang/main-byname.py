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
        self.setWindowTitle("牛筋草抗药性水平查询系统")
        self.resize(1280,200)
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
        self.gtTabgwt = QTableWidget(self)
        self.gtTabgwt.setRowCount(3)
        self.gtTabgwt.setColumnCount(17)
        self.gtTabgwt.setHorizontalHeaderLabels(['种群','穗分枝数(个)','分支籽粒充实度(%)','a','b','R2','GR50(g a.i.ha-1)','95%置信区间(GR50)','IR','a','b','R2','GR50(g a.i.ha-1)','95%置信区间(GR50)','IR','采样地点','生境'])
        #self.tmodel.setHorizontalHeaderLabels(
        
        #['种群','穗分枝数(个)','分支籽粒充实度(%)','a','b','R2','GR50(g a.i.ha-1)','95%置信区间(GR50)','IR','a','b','R2','GR50(g a.i.ha-1)','95%置信区间(GR50)','IR','采样地点','生境'])
        """
        self.tableView = QTableView(self)
        self.tableView.setModel(self.tmodel)
        self.tableView.setShowGrid(True)
        """

        self.hlayout_table.addWidget(self.gtTabgwt)
 
        self.hwg_s = QWidget(self)
        self.hwg_t = QWidget(self)
        #self.gtTabgwt.setColumnHidden(0,True)
        self.gtTabgwt.verticalHeader().setVisible(False)

        self.gtTabgwt.horizontalHeader().setVisible(False)
        
        self.hwg_s.setLayout(self.hlayout_Search)
        self.hwg_t.setLayout(self.hlayout_table)
        
        
        level_1 = ['种群','穗分枝数(个)','分支籽粒充实度(%)','a','b','R2','GR50(g a.i.ha-1)','95%置信区间(GR50)','IR','a','b','R2','GR50(g a.i.ha-1)','95%置信区间(GR50)','IR','采样地点','生境']
        
        self.gtTabgwt.setSpan(0,0,2,1)
        self.gtTabgwt.setSpan(0,1,1,2)
        #self.gtTabgwt.setSpan(0,2,2,1)
        self.gtTabgwt.setSpan(0,3,1,6)
        #self.gtTabgwt.setSpan(0,4,2,1)
        #self.gtTabgwt.setSpan(0,5,2,1)
        #self.gtTabgwt.setSpan(0,6,2,1)
        #self.gtTabgwt.setSpan(0,7,2,1)
        #self.gtTabgwt.setSpan(0,8,2,1)
        self.gtTabgwt.setSpan(0,9,1,6)
        #self.gtTabgwt.setSpan(0,10,2,1)
        #self.gtTabgwt.setSpan(0,11,2,1)
        #self.gtTabgwt.setSpan(0,12,2,1)
        #self.gtTabgwt.setSpan(0,13,2,1)
        #self.gtTabgwt.setSpan(0,14,2,1)
        self.gtTabgwt.setSpan(0,15,1,2)
        #self.gtTabgwt.setSpan(0,16,2,1)
        self.gtTabgwt.setRowHeight(0,10)
        self.gtTabgwt.setRowHeight(1,10)
        
        self.gtTabgwt.setItem(0,0,QTableWidgetItem("种群"))
        self.gtTabgwt.setItem(0,1,QTableWidgetItem("形态指标"))
        self.gtTabgwt.setItem(1,1,QTableWidgetItem("穗分枝数(个)"))
        self.gtTabgwt.setItem(1,2,QTableWidgetItem("分支籽粒充实度(%)"))
        self.gtTabgwt.setItem(0,3,QTableWidgetItem("对百草枯的抗药性水平"))
        self.gtTabgwt.setItem(1,3,QTableWidgetItem("a"))
        self.gtTabgwt.setItem(1,4,QTableWidgetItem("b"))
        self.gtTabgwt.setItem(1,5,QTableWidgetItem("R2"))
        self.gtTabgwt.setItem(1,6,QTableWidgetItem("GR50(g a.i.ha-1)"))
        self.gtTabgwt.setItem(1,7,QTableWidgetItem("95%置信区间(GR50)"))
        self.gtTabgwt.setItem(1,8,QTableWidgetItem("IR"))
        
        
        self.gtTabgwt.setItem(0,9,QTableWidgetItem("对草甘膦的抗药性水平"))
        self.gtTabgwt.setItem(1,9,QTableWidgetItem("a"))
        self.gtTabgwt.setItem(1,10,QTableWidgetItem("b"))
        self.gtTabgwt.setItem(1,11,QTableWidgetItem("R2"))
        self.gtTabgwt.setItem(1,12,QTableWidgetItem("GR50(g a.i.ha-1)"))
        self.gtTabgwt.setItem(1,13,QTableWidgetItem("95%置信区间(GR50)"))
        self.gtTabgwt.setItem(1,14,QTableWidgetItem("IR"))
        self.gtTabgwt.setItem(0,15,QTableWidgetItem("采集地点及用药史"))
        self.gtTabgwt.setItem(1,15,QTableWidgetItem("采样地点"))
        self.gtTabgwt.setItem(1,16,QTableWidgetItem("生境"))
        self.gtTabgwt.setLineWidth(2)
        #print(dir(self.gtTabgwt))
        #self.gtTabgwt.setTextAlignment(Qt.AlignHCenter)
        
        #self.gtTabgwt.setColumnWidth(0,20)

        
        
        self.gWg.addWidget(self.hwg_s)
        self.gWg.addWidget(self.hwg_t)
        self.setLayout(self.gWg)
        self.gtTabgwt.resizeColumnsToContents()
        self.gtTabgwt.resizeRowsToContents()
        
        #self.gtTabgwt.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    def getSearchText(self):
        #print(self.qle.text())
        
        self.searchText = self.qle.text()
        self.retList = searchData(self.searchText,self.workList)
        print(self.retList)
        for index in range(0,16,1):
            item = QTableWidgetItem('')
            self.gtTabgwt.setItem(2,index,item)
        if len(self.retList) == 0:
            print("没有搜索到该种群")
        else:
            try:
                tableList = [self.retList[0][0],self.retList[2][1],self.retList[2][2],self.retList[0][1],self.retList[0][2],self.retList[0][3],self.retList[0][4],self.retList[0][5],self.retList[0][6],self.retList[1][1],self.retList[1][2],self.retList[1][3],self.retList[1][4],self.retList[1][5],self.retList[1][6],self.retList[3][1],self.retList[3][2]]
                #print(tableList)
                #self.gtTabgwt.clear()
                for index,line in enumerate(tableList):
                    item = QTableWidgetItem(line)
                    self.gtTabgwt.setItem(2,index,item)
                self.gtTabgwt.resizeColumnsToContents()
                self.gtTabgwt.resizeRowsToContents()
                #self.gtTabgwt.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            except:
                pass
            
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


