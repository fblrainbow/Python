#coding:utf-8
import os
import sys
import xlrd
import xlwt
from xlutils.copy import copy
from datetime import datetime

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
        
    """ 
    print(table_0.cell(1,1).value)
    print(table_0.ncols,table_0.nrows)
    #print(dir(table_0))
    """
def searchData(string,objTable):
    
    objDataList = []
    for index,singleTable in enumerate(objTable):
        for line in singleTable[1:]:
            if line[0] == string:
                objDataList.append(line)
    return objDataList





if __name__ == "__main__":
    workList = openWorkBook("csj.xlsx")

    
    #print(sheet_4[0])
    """
    for sheet in workList:
        for row in sheet:
            print(row)
        print("\n\n")
    """
    retList = searchData("MZ04",workList)
    print(retList)


