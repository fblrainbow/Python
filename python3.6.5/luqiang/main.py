#coding:utf-8
import os
import sys
import re
from bs4 import BeautifulSoup
from urllib import request
import xlrd 
# from xlwt import *
import xlwt
from xlutils.copy import copy
from datetime import datetime

def openWorkBook(fileName):
    workbook = xlrd.open_workbook(fileName)
    #print(dir(workbook))
    sheetCount = len(workbook.sheets())
    workList = []
    for i in range(0,sheetCount,1):
        tmpTable = workbook.sheets()[i]
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
    
    
if __name__ == "__main__":
    workList = openWorkBook("csj.xlsx")
    #不同种群牛筋草对百草枯的抗药性水平
    sheet_0 = workList[0]
    #不同种群牛筋草对草甘膦的抗药性水平
    sheet_1 = workList[1]
    #不同种群牛筋草对草铵膦的抗药性水平
    sheet_2 = workList[2]
    #不同种群牛筋草穗部形态指标调查
    sheet_3 = workList[3]
    #不同种群牛筋草种植采集地点及用药史
    sheet_4 = workList[4]
    #如何查询
    sheet_5 = workList[5]
    sheet_6 = workList[6]
    
    print(sheet_1[0])
    """
    for sheet in workList:
        for row in sheet:
            print(row)
        print("\n\n")
    """


