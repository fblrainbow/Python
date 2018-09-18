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
	'Cookie':'uuid_tt_dd=10_30709689370-1528124825427-783725; TY_SESSION_ID=dc063d97-5415-4514-96cf-b381d472c223; __yadk_uid=MqWqFmWVPVEIdlECYlDAbDhaKwjW9U6T; UserName=weixin_42090936; UserInfo=BxizQLbnNgSeuSg45l%2B9n6jMaA1IYkSRvMvXODhm7wpE%2B00DHqDT56Tn5NunJd48QEReOgp86zX%2BXXh7594x3Q%3D%3D; UserNick=weixin_42090936; UN=weixin_42090936; AU=B2D; BT=1528298452666; smidV2=201806061520375b113891b65b8033e55cef20828cd95e00f0814663c16a3c0; ADHOC_MEMBERSHIP_CLIENT_ID1.0=53631aff-692b-6933-eaf0-54680bc37997; dc_tos=p9w4l9; dc_session_id=10_1528124825427.189552; Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac=1528128020,1528129182,1528199412,1528264737; Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac=1528269926'	
	}
# cookies = {
# 	'Cookie':'uuid_tt_dd=10_30709689370-1528124825427-783725; TY_SESSION_ID=dc063d97-5415-4514-96cf-b381d472c223; __yadk_uid=MqWqFmWVPVEIdlECYlDAbDhaKwjW9U6T; UserName=weixin_42; UserInfo=BxizQLbnNgSeuSg45l%2B9n6jMaA1IYkSRvMvXODhm7wpE%2B00DHqDT56Tn5NunJd48QEReOgp86zX%2BXXh7594x3Q%3D%3D; UserNick=weixin_42090936; UN=weixin_42090936; AU=B2D; BT=1528298452666; smidV2=201806061520375b113891b65b8033e55cef20828cd95e00f0814663c16a3c0; ADHOC_MEMBERSHIP_CLIENT_ID1.0=53631aff-692b-6933-eaf0-54680bc37997; dc_tos=p9w4l9; dc_session_id=10_1528124825427.189552; Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac=1528128020,1528129182,1528199412,1528264737; Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac=1528269926'	
# 	}
# 
headers = {
	'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.5155.400 QQBrowser/9.7.13231.400'
}
cookies = {
	'Cookie':'uuid_tt_dd=10_30709689370-1528124825427-783725; TY_SESSION_ID=dc063d97-5415-4514-96cf-b381d472c223; __yadk_uid=MqWqFmWVPVEIdlECYlDAbDhaKwjW9U6T; UserName=weixin_42090936; UserInfo=BxizQLbnNgSeuSg45l%2B9n6jMaA1IYkSRvMvXODhm7wpE%2B00DHqDT56Tn5NunJd48QEReOgp86zX%2BXXh7594x3Q%3D%3D; UserNick=weixin_42090936; UN=weixin_42090936; AU=B2D; BT=1528298452666; smidV2=201806061520375b113891b65b8033e55cef20828cd95e00f0814663c16a3c0; __utma=17226283.826590548.1528276993.1528276993.1528276993.1; __utmc=17226283; __utmz=17226283.1528276993.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); ADHOC_MEMBERSHIP_CLIENT_ID1.0=53631aff-692b-6933-eaf0-54680bc37997; dc_tos=p9x31y; dc_session_id=10_1528124825427.189552; Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac=1528313069,1528313400,1528313612,1528313614; Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac=1528314560'

}
# url = 'https://blog.csdn.net/weixin_39599711/article/list'
url = 'https://blog.csdn.net/qq_37608398/article/list/'
timeMode1 = int(time.time())
print(timeMode1)   #1528314372
def getHtmlCode(url):
	# timeMode = 1 + 42090936
	# print(time)
	# cookiesValue = 'uuid_tt_dd=10_30709689370-1528124825427-783725; TY_SESSION_ID=dc063d97-5415-4514-96cf-b381d472c223; __yadk_uid=MqWqFmWVPVEIdlECYlDAbDhaKwjW9U6T; ' + 'UserName=weixin_' + str(timeMode) + ';' + 'UserInfo=BxizQLbnNgSeuSg45l%2B9n6jMaA1IYkSRvMvXODhm7wpE%2B00DHqDT56Tn5NunJd48QEReOgp86zX%2BXXh7594x3Q%3D%3D; ' + 'UserNick=weixin_' + str(timeMode) + '; ' + 'UN=weixin_' + str(timeMode) + ';' + 'AU=B2D; '
	# cookies = {}
	# cookies['Cookie'] = cookiesValue
	# print(cookies) 
	htmlResponse = requests.get(url,cookies=cookies,headers=headers)
	if 200 != htmlResponse.status_code:
		print('请求失败!')
	htmlResponse.encoding = 'utf-8'
	# htmlResponse
	htmlCode = htmlResponse.text
	# print(htmlCode)
	htmlCode.encode('utf-8')
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
while True:	
	t1 = personTotle(url)
	personalInfo = t1.getPersonalInfo()
	personalInfoJson = json.dumps(personalInfo)
	print(personalInfo)
	f = open('记录.json','a+')
	f.write(personalInfoJson)
	f.write('\n')
	f.close()
	for count in range(1,4):
	 	t1.getArticleInfo(count)
	time.sleep(3)



url = 'https://blog.csdn.net/qq_37608398/article/list/'
# https://blog.csdn.net/qq_37608398/article/details/80574931
# https://blog.csdn.net/qq_37608398/article/78163086