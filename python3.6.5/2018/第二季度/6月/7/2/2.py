#!/usr/bin/env python3
#coding:utf-8

import requests
from bs4 import BeautifulSoup
import os
import re
import sys
import datetime
import json
import time

cookies = {
	'Cookie':'uuid_tt_dd=10_30709696920-1528316589965-629560; smidV2=20180607042305ddd86f064652dd42b22e7d0113d40f00000ae092306db6d90; UserName=qq_37608398; UserInfo=YleRigef8jqAcRgUEr8XfvnHyGiTFj91IMxMdgCPhEzSSyUbrddA4mExsrlGQYhg5bZ3AaqyG1QoxLTiGd1kTsZSxyk7VQOSiobYpZKfFY4%3D; UserNick=RainbowJhon; UN=qq_37608398; AU=2FB; BT=1528316609795; TY_SESSION_ID=2cc9967b-e815-4ced-89dc-687e5a873774; Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac=1528316586; Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac=1528316624; dc_tos=p9x4nj; dc_session_id=10_1528316589965.919817'
	}
cookies = {
	'Cookie':'uuid_tt_dd=10_30709696920-1528316589965-629560; smidV2=20180607042305ddd86f064652dd42b22e7d0113d40f00000ae092306db6d90; UserName=qq_37608398; UserInfo=YleRigef8jqAcRgUEr8XfvnHyGiTFj91IMxMdgCPhEzSSyUbrddA4mExsrlGQYhg5bZ3AaqyG1QoxLTiGd1kTsZSxyk7VQOSiobYpZKfFY4%3D; UserNick=RainbowJhon; UN=qq_37608398; AU=2FB; BT=1528316609795; TY_SESSION_ID=2cc9967b-e815-4ced-89dc-687e5a873774; Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac=1528316586; Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac=1528316624; dc_tos=p9x4nj; dc_session_id=10_1528316589965.919817'
	}
headers = {
	'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.5155.400 QQBrowser/9.7.13231.400'
}
url = 'https://blog.csdn.net/qq_37608398/article/list/'
# url = 'https://blog.csdn.net/yong318585/article/list/'


def getHtmlCode(url):
	# timeMode = int(time.time()) % 42000000
	# # print(time)
	# cookiesValue = 'UserName=weixin_' + str(timeMode) + ';' + 'UserNick=weixin_' + str(timeMode) + '; ' + 'UN=weixin_' + str(timeMode) + ';'
	# # cookies = {}
	# cookies['Cookie'] = cookiesValue
	# print(cookies) 
	htmlResponse= requests.get(url,cookies=cookies,headers=headers)
	if 200 != htmlResponse.status_code:
		print('请求失败!')
	htmlResponse.encoding = 'utf-8'
	# htmlResponse
	htmlCode = htmlResponse.text
	htmlCode.encode('utf-8')
	# print(htmlCode)
	return htmlCode
def getHtmlTree(url):
	htmlCode = getHtmlCode(url)
	htmlTree = BeautifulSoup(htmlCode,'html.parser')
	return htmlTree
# print(getHtmlTree(url))
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
class personTotle:
	def __init__(self,url):
		self.url = url
	def getPersonalInfo(self):
		personalInfo = {}
		htmlTree = getHtmlTree(self.url)
		classDataInfo = htmlTree.find('div',class_='data-info d-flex item-tiling')
		classTextCenterList = classDataInfo.find_all('dl',class_='text-center')
		personalInfoDict = {}
		personalInfoDict[classTextCenterList[0].dt.a.get_text()] = classTextCenterList[0].dd.a.span.get_text()
		personalInfoDict[classTextCenterList[1].dt.get_text()] = classTextCenterList[1].dd.span.get_text()
		personalInfoDict[classTextCenterList[2].dt.get_text()] = classTextCenterList[2].dd.span.get_text()
		personalInfoDict[classTextCenterList[3].dt.get_text()] = classTextCenterList[3].dd.span.get_text()
		# print(personalInfoDict)

		classGradeinfo = htmlTree.find('div',class_='grade-box clearfix')
		classGradeinfoList = classGradeinfo.find_all('dl')
		personalGradeInfoDict = {}
		personalGradeInfoDict[classGradeinfoList[0].dt.get_text().replace('：','')]=classGradeinfoList[0].a['title'].split(',')[0]
		personalGradeInfoDict[classGradeinfoList[1].dt.get_text().replace('：','')]=classGradeinfoList[1].dd['title']
		personalGradeInfoDict[classGradeinfoList[2].dt.get_text().replace('：','')]=classGradeinfoList[2].dd['title']
		personalGradeInfoDict[classGradeinfoList[3].dt.get_text().replace('：','')]=classGradeinfoList[3]['title']
		# print(personalGradeInfoDict)

		personalNick = htmlTree.find('h2',class_='title-blog').get_text().replace(' ','').replace('\n','')
		# print(personalNick)
		nowTime=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

		personalInfo['Time'] = nowTime
		personalInfo['Author'] = personalNick	
		personalInfo['Ability'] = personalInfoDict
		personalInfo['Contrbute'] = personalGradeInfoDict
		return personalInfo
	def getArticleInfo(self,count):
		tmpUrl = self.url + str(count)
		htmlTree = getHtmlTree(tmpUrl)
		articleInfoDictCount = {}
		try:
			personalArticleContent = htmlTree.find('div',class_='article-list')
			personalArticleContentList = personalArticleContent.find_all('div',class_='article-item-box csdn-tracking-statistics')
			articleInfo = {}
			times = 0
			for line in personalArticleContentList:
				articleInfoDict = {}
				articleInfoDict['articleUrl'] = line.h4.a['href']
				tmp = getHtmlTree(articleInfoDict['articleUrl'])
				print(tmp)
				print(articleInfoDict['articleUrl'])
				break
				articleInfoDict['articleTitle'] = line.h4.get_text().replace(' ','').replace('\n','')[1:]
				articleInfoDict['articleWriteDate'] = line.find('span',class_='date').get_text()
				articleInfoDict['articleReadTimes'] = line.find_all('span',class_='read-num')[0].get_text()
				articleInfoDict['articleRemarkTimes'] = line.find_all('span',class_='read-num')[1].get_text()
				articleInfo[str(times)] = articleInfoDict
				times = times + 1
			articleInfoDictCount[str(count)] = articleInfo
			return articleInfoDictCount
		except:
			pass


# while True:	
t1 = personTotle(url)
personalInfo = t1.getPersonalInfo()
personalInfoJson = json.dumps(personalInfo)

# print(personalInfo)

f = open('记录.json','a+')
f.write(personalInfoJson)
f.write('\n')
f.close()
for count in range(1,4):
	t1.getArticleInfo(count)
	break
time.sleep(3)


url = 'https://blog.csdn.net/qq_37608398/article/list/'
