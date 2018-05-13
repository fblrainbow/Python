#!/usr/bin/env python3
#coding:utf-8

import re
import os
import sys
import requests
from bs4 import BeautifulSoup
import xlrd
import xlwt
from xlutils.copy import copy
import time
def isDefine(var):
	try:
		type(var)
	except NameError:
		print('变量%s未定义'%var)
	except:
		pass
def writeJudge(fileName,count):
	workBook = xlrd.open_workbook(fileName)
	table = workBook.sheets()[0]
	try:
		table.cell(count,1).value
		print(table.cell(count,0).value)
		if '' != table.cell(count,0).value:
			print('skip')
			return True
	except IndexError:
		return False
def writeExcel(fileName,dataList,count):	
	workBook = xlrd.open_workbook(fileName)
	table = workBook.sheets()[0]
	dataList.insert(0,str(count))
	newBook = copy(workBook)
	dataSheet = newBook.get_sheet('sheet1')
	for j in range(0,table.ncols):
		tmp = str(dataList[j])
		tmp = tmp.replace('\n','').replace(' ','')
		dataSheet.write(count,j,tmp)
	newBook.save(fileName)
def readExcel(fileName):
	workBook = xlrd.open_workbook(fileName)
	table = workBook.sheets()
	print(len(table))
	print(table.sort)
	print(table[2].name)
readExcel('excel.xlsx')