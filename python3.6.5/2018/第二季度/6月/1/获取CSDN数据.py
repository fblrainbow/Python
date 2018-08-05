#!/usr/bin/env python3
#coding:utf-8

import requests
from bs4 import BeautifulSoup
import os
import re
import sys

cookies = {
	'Cookie':'uuid_tt_dd=10_30709694610-1527791691256-470312; UserName=qq_37608398; UserInfo=YleRigef8jqAcRgUEr8XfvnHyGiTFj91IMxMdgCPhEzSSyUbrddA4mExsrlGQYhg5bZ3AaqyG1QoxLTiGd1kTsZSxyk7VQOSiobYpZKfFY4%3D; UserNick=RainbowJhon; UN=qq_37608398; AU=2FB; BT=1527852570586; Hm_ct_6bcd52f51e9b3dce32bec4a3997715ac=1788*1*PC_VC; smidV2=20180601192836bf3e650eaaa41b4e25a7181e3aa97a1000ce4894db65a9a20; dc_tos=p9n8eg; dc_session_id=10_1527791691256.526264; Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac=1527791688,1527853147,1527853186; Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac=1527854920'
	}

headers = {
	'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.5155.400 QQBrowser/9.7.13231.400'
}
url = 'https://my.csdn.net/my/follow'

def getHtmlCode(url):
	htmlResponse= requests.get(url,cookies=cookies,headers=headers)
	if 200 != htmlResponse.status_code:
		print('请求失败!')
	print(dir(htmlResponse))
	htmlCode = htmlResponse.text
	
	return htmlCode
def getHtmlTree(url):
	htmlCode = getHtmlCode(url)
	htmlTree = BeautifulSoup(htmlCode,'html.parser')
	return htmlTree
def getOn(url):	
	htmlTree = getHtmlTree(url)
	getAtag = htmlTree.find('a',class_='on')
	aTagContent = getAtag.text
	count = aTagContent[5:-1]
	number = int(count)
	# print(type(number))
	return number
def getKeyDict(url):
	htmlTree = getHtmlTree(url)
	dictRow = {}
	listRow = htmlTree.find_all('div',class_='col-sm-6')
	for row in listRow:
		tmp = row.dt.a
		href = 'https://my.csdn.net' + tmp['href']
		personalWeb = getHtmlTree(href)
		UserNameContent = personalWeb.find('span')
		dictRow[UserNameContent.text] = href
	# print(dictRow)
	return dictRow
def todo(url):
	number = getOn(url)
	if 0 != (number%20):
		count = int(number / 20 + 1)
	# print(count)
	dictRow = {}
	for page in range(1,count+1): 
		pageUrl = url + '/' + str(page)
		# print(pageUrl)
		dictRowTmp = getKeyDict(pageUrl)
		for k,v in dictRowTmp.items():
			dictRow[k] = v
	print(dictRow)
url = 'https://my.csdn.net/jerry_1126'
class personTotle:
	def __init__(self,url):
		self.url = url
	def getKeyInfo(self):
		htmlTree = getHtmlTree(self.url)
		pageCount = htmlTree.find('div',class_='csdn-pagination').get_text()
		indexHead = pageCount.find('共')
		pageCount = pageCount[indexHead+2:]
		indexHead = pageCount.find('共')
		# print(indexHead)
		indexEnd = pageCount.find('页')
		pageCount = int(pageCount[indexHead+1:indexEnd])
		return pageCount
	def getArticle(self,url):
		# self.url = url
		htmlTree = getHtmlTree(self.url)
		article = htmlTree.find_all('li',class_='clearfix')
		for line in article:
			lineText = line.find('span',class_='dTime').get_text()
			lineAtag = line.a
			lineAhref = lineAtag['href']
			lineAtitle = lineAtag['title']
			print(lineText,lineAhref,lineAtitle)
# t1 = personTotle(url)
# pageCount = t1.getKeyInfo()
# for line in range(1,pageCount+1):
# 	tmpUrl = url + '/' + str(line)
# 	t1.getArticle(tmpUrl)

url = 'https://my.csdn.net/my/home/get_user_blog?username=u014775175&page=2'
getHtmlTree(url)