#!/usr/bin/env python3
#!coding:utf-8
import os
import re
import requests
import sys
import datetime
import json
import time
from bs4 import BeautifulSoup
cookies = {
'Cookie':'uuid_tt_dd=10_30709697800-1528894478107-222451; TY_SESSION_ID=71d7ab0a-5f0c-48b6-9cf7-e419a2c0094e; __yadk_uid=QZsf7vezSZzKYl2M6abAssYi8lJcUkBz; smidV2=20180614135440ec11f760bdab45ec00a2c39837fee366006335f82eedfb5d0; dc_session_id=10_1528894478107.508397; UserName=qq_37498115; UserInfo=nfih5Jf%2F3Mbg4pAgoaBKZGUOrD0K4JHk8x1paMxRXNoVWp3YjqBOfxlmXyk6H6I7StEB2qAH5B6yWnIQ%2FzIYvA%3D%3D; UserNick=qq_37498115; UN=qq_37498115; AU=C48; BT=1528984564764; dc_tos=pabg2t; Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac=1528955555,1528955563,1528955668,1528984502; Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac=1528984613'
}
headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.5155.400 QQBrowser/9.7.13231.400'
}
# url = 'https://blog.csdn.net/axuhongbo/phoenix/comment/submit?id=80669319'
submit_url = 'https://blog.csdn.net/qq_37608398/phoenix/comment/submit?id=80659961'
submit_url_header = 'https://blog.csdn.net/qq_37608398/phoenix/comment/submit?id='

# data = {"count":1,"page_count":1,"floor_count":1,"list":[{"info":{"CommentId":"8106897","ArticleId":"79072691","BlogId":"7358822","ParentId":"0","PostTime":"2018-06-13 00:50:10","Content":"\u597d\u5389\u5bb3\u7684\u6837\u5b50","UserName":"qq_37608398","Status":"0","IP":"183.11.38.201","IsBoleComment":"0","PKId":"0","Digg":"0","Bury":"0","SubjectType":"-1","WeixinArticleId":"0","Avatar":"https:\/\/avatar.csdn.net\/2\/F\/B\/3_qq_37608398.jpg"}}]}
data = {'replyId':'','content':'厉害了，谢谢分享！'}

def Post(url):
	response = requests.post(url = url,data = data,cookies = cookies,headers = headers)
	json_obj = response.text
	json_str = json.loads(json_obj)
	print(json_str['content'])
	return json_str['result']

	# print(response.status_code)
# Post(url)
url = 'https://blog.csdn.net/qq_37608398/article/list/'
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
		print(htmlResponse.status_code)
	htmlResponse.encoding = 'utf-8'
	# htmlResponse
	htmlCode = htmlResponse.text
	# print(htmlCode)
	htmlCode.encode('utf-8')
	return htmlCode
# print(getHtmlCode(url))
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
				# print(articleInfoDict['articleUrl'])
				articleUrlSlove = articleInfoDict['articleUrl'].split('/')
				submit_url = submit_url_header + articleUrlSlove[-1]
				# Post(submit_url)
				tmp = getHtmlTree(articleInfoDict['articleUrl'])
				articleInfoDict['articleTitle'] = line.h4.get_text().replace(' ','').replace('\n','')[1:]
				articleInfoDict['articleWriteDate'] = line.find('span',class_='date').get_text()
				articleInfoDict['articleReadTimes'] = line.find_all('span',class_='read-num')[0].get_text()
				articleInfoDict['articleRemarkTimes'] = line.find_all('span',class_='read-num')[1].get_text()
				articleInfo[str(times)] = articleInfoDict
				times = times + 1
			articleInfoDictCount[str(count)] = articleInfo
			# print(articleInfo)
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
	for count in range(1,3):
	 	t1.getArticleInfo(count)
	time.sleep(10)
	# 18126379694
	# https://blog.csdn.net/testcs_dn/article/details/43498997