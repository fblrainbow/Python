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
url = 'http://www.biqiuge.com/book/37708/'
url = 'http://www.biqiuge.com/book/'
def getHtmlTree(url):
	webPage = request.urlopen(url)
	htmlCode = webPage.read()
	htmlTree = BeautifulSoup(htmlCode,'html.parser')
	return htmlTree
xlsName = r'2.xls'
#判断网页是否存在
def adjustExist(url):
	try:  
		htmlTree=getHtmlTree(url)
		title = htmlTree.h1.get_text()
		author = htmlTree.find_all('meta',property="og:novel:author")
		author = author[0]['content']
		txtSize = htmlTree.find('div',id='info')
		# txtSize = str(txtSize[0])
		# pattern = re.compile(r'[(.*)]')
		# txtSize = pattern.findall(txtSize)
		txtSize = txtSize.find_all('p')
		txtSize = str(txtSize)
		# pattern = re.compile('[(.*)]')
		# txtSize = pattern.findall(txtSize)
		flag1 = txtSize.find('共')
		flag2 = txtSize.find('字')
		if -1 == flag1 or -1 == flag2:
			txtSize = ''
		else: 
			txtSize = txtSize[flag1:flag2+1]
		if u'出现错误！-笔趣阁' == title:
			print(url + '    不存在！')
		else:
			print(url)
			# print(title)
	except:
		author = 'fbl'
		txtSize = '0 bytes'
		title = 'Unknow'
		pass
	finally:
		return (author,txtSize ,title)
def main():
	reWriteFlag = False
	start_url = 6000
	end_url = 30000
	if start_url > end_url:
		(end_url,start_url) = (start_url,end_url)
	# start_url = 40000
	# end_url = 40001
	#init = [u'序号',u'小说名',u'字数',u'作者',u'路径']
	# workbook = xlwt.Workbook(encoding = 'utf-8')
	# data_sheet = workbook.add_sheet(u'笔趣阁小说')
	fileName = u'笔趣阁.xls'
	workbook = xlrd.open_workbook(fileName,formatting_info=True)
	# newBook = copy(workbook)
	# data_sheet = newBook.get_sheet(u'笔趣阁小说')
	if reWriteFlag:
		# old_sheet = workbook.sheet_by_name(u'笔趣阁小说')
		newBook = copy(workbook)
		data_sheet = newBook.get_sheet(u'笔趣阁小说')
		for i in range(len(init)):
			data_sheet.write(0,i,init[i])
		newBook.save(fileName)
	for j in range(start_url,end_url):
		workbook = xlrd.open_workbook(fileName,formatting_info=True)
		table = workbook.sheets()[0]
		try:
			cell_value = table.cell(j,0).value
			# print(type(cell_value))
			if cell_value != '':
				print(cell_value)
				continue
		except:
			print('NLL')
			pass
		url_tmp = url + str(j)
		(author,size,title) = adjustExist(url_tmp)
		tmp = [j,title,size,author,url_tmp]
		newBook = copy(workbook)
		data_sheet = newBook.get_sheet(u'笔趣阁小说')
		# data_sheet = newBook.sheet_by_name(u'笔趣阁小说')

		# print(cell_value)
		for k in range(len(tmp)):
			data_sheet.write(j,k,tmp[k])
		newBook.save(fileName)
main()


# workbook = xlwt.Workbook(encoding = 'utf-8')
# data_sheet = workbook.add_sheet(u'biqiuge')

# row0 = [u'字段名称', u'大致时段', 'CRNTI', 'CELL-ID']  
# row1 = [u'测试', '15:50:33-15:52:14', 22706, 4190202]  

# #生成第一行和第二行  
# for i in range(len(row0)):  
# 	data_sheet.write(0, i, row0[i])  
# 	data_sheet.write(1, i, row1[i])  

# #保存文件  
# workbook.save('demo.xls')     
      

# book = open_workbook(xlsName)
# wb = copy(book)
# s = wb.get_sheet(1)
# # s = book.get_sheet(1)
# s.write(0,1,"new data")
# s.write(0,0,"dsfa")
# wb.save("new_data.xls")

# main()
# xlsFileName = '1.xls'
# book = xlrd.open_workbook(xlsFileName)
# sheet_name = book.sheet_names()
# print(sheet_name)
# sheet1 = book.sheet_by_index(1)
# print(sheet1)
# nrows = sheet1.nrows
# ncols = sheet1.ncols
# print(nrows,ncols)
# row_data = sheet1.cell_value(1,1)
# print(row_data)


# xlsName = r'2.xls'
# rb = xlwt.Workbook()

# sheet = rb.add_sheet(u'sheet2',cell_overwrite_ok = True)
# sheet.write(0,0,'fbl')
# rb.save(xlsName)

