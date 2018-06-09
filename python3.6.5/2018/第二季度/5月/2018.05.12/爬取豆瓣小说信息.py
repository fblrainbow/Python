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

cookies = {
	'Cookie':'bid=_lOjPCNt9wI; ll="118282"; _vwo_uuid_v2=90A455F697D39C4E7ADE716F87221D41|b2cfd7bec4a7b17a840474041b898d19; \
	__utmz=30149280.1515430997.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1526163393%2C%22https%3A%2F%2F\
	www.baidu.com%2Flink%3Furl%3Di67U7qyjj2YTlYZQ70NdqBclRhph70YnxXtUfm9GbohY-oTCGvexr5jVK2HlN14Cx7jduO8mqrITN9howpYm5a%26wd%3D%26eqid%3Dc4b93c230000ef1f000000065a53a449%22%5D;\
	 _pk_ses.100001.8cb4=*; __utma=30149280.1644812988.1515427525.1520879588.1526163394.4; __utmc=30149280; __utmt=1; dbcl2="178599165:CHlk4aEqUAA";\
	  _ga=GA1.2.1644812988.1515427525; _gid=GA1.2.1120993180.1526163442; _gat_UA-7019765-1=1; ck=wUb_; _pk_id.100001.8cb4=51c8326516a16325.1515430996.2.1526163443.1515430996.;\
	   push_noty_num=0; push_doumail_num=0; __utmv=30149280.17859; __utmb=30149280.4.10.1526163394; ct=y; __yadk_uid=1UDWf6kQP5PYke9rFuHb2klf4KbW2B5R'
}
cookies = {
	'Cookie':'bid=_lOjPCNt9wI; ll="118282"; _vwo_uuid_v2=90A455F697D39C4E7ADE716F87221D41|b2cfd7bec4a7b17a840474041b898d19; __utmc=30149280; _ga=GA1.2.1644812988.1515427525; _gid=GA1.2.1120993180.1526163442; push_noty_num=0; push_doumail_num=0; ct=y; __yadk_uid=1UDWf6kQP5PYke9rFuHb2klf4KbW2B5R; _pk_ses.100001.8cb4=*; __utma=30149280.1644812988.1515427525.1526171405.1526171405.1; __utmz=30149280.1526171405.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; dbcl2="178599165:Y53LLRSxUvs"; _gat_UA-7019765-1=1; ck=QzdS; _pk_id.100001.8cb4=8ab848a65c47cc4a.1526171404.1.1526171408.1526171404.; __utmv=30149280.17859; __utmb=30149280.3.10.1526171405'
	# 'Cookie':'bid=_lOjPCNt9wI; ll="118282"; _vwo_uuid_v2=90A455F697D39C4E7ADE716F87221D41|b2cfd7bec4a7b17a840474041b898d19; __utmc=30149280; _ga=GA1.2.1644812988.1515427525; _gid=GA1.2.1120993180.1526163442; push_noty_num=0; push_doumail_num=0; __utmv=30149280.17859; ct=y; __yadk_uid=1UDWf6kQP5PYke9rFuHb2klf4KbW2B5R; gr_user_id=c8ba5876-e51d-4ef0-a9a9-74732a8cafeb; gr_cs1_53914151-1bda-41c7-9211-36725e7d02fd=user_id%3A1; gr_session_id_22c937bbd8ebd703f2d8e9445f7dfd03=53914151-1bda-41c7-9211-36725e7d02fd_true; ps=y; ue="204206705@qq.com"; dbcl2="178599165:DNtWos6aGXg"; ck=j8y7; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1526171226%2C%22https%3A%2F%2Faccounts.douban.com%2Fsafety%2Funlock_sms%2Fresetpassword%3Fconfirmation%3Ded7ec7f5a5ec4aad%26alias%3D%22%5D; _pk_id.100001.8cb4=51c8326516a16325.1515430996.3.1526171226.1526163456.; _pk_ses.100001.8cb4=*; __utma=30149280.1644812988.1515427525.1526168455.1526171227.6; __utmz=30149280.1526171227.6.3.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/safety/unlock_sms/resetpassword; __utmt=1; __utmb=30149280.1.10.1526171227'
}

headers = {
	'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}
url = 'https://book.douban.com/subject/3359946/'
url = 'https://book.douban.com/subject/26853356/'
# url = 'https://book.douban.com/subject/27035185/'
# url = 'https://book.douban.com/subject/22227388/'
def getHtmlTree(url):
	# time.sleep(3)
	tmp = requests.get(url,cookies = cookies,headers = headers)
	if 200 != tmp.status_code:
		print('请求异常，返回码为%s'%tmp.status_code)
		exit()
	text = tmp.text
	htmlTree = BeautifulSoup(text,'html.parser')
	return htmlTree
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
	# try:
	# 	table.cell(count,0).value
	# 	if None != table.cell(count,0).value:
	# 		print('skip')
	# 		return
	# except IndexError:
	# 	pass
	dataList.insert(0,str(count))
	newBook = copy(workBook)
	dataSheet = newBook.get_sheet('sheet1')
	for j in range(0,table.ncols):
		tmp = str(dataList[j])
		tmp = tmp.replace('\n','').replace(' ','')
		dataSheet.write(count,j,tmp)
	newBook.save(fileName)

def getKeyWord(url):
	htmlTree = getHtmlTree(url)
	storyName = htmlTree.find('span',property="v:itemreviewed").get_text().replace(' ','').replace('\n','')
	storyInfo = htmlTree.find('div',id='info')
	storyInfoList = storyInfo.findAll('span')
	storyAuthor = ''
	storyPublish = ''
	storyDate = ''
	storyPages = ''
	storyPrices = ''
	storyGetUp = ''
	storyTotleName =''
	storyISBN = ''
	for line in storyInfoList:
		try:
			if -1 != line.get_text().find('作者'):
				storyAuthor = line.nextSibling.nextSibling.get_text().replace(' ','').replace('\n','')
		except AttributeError:
			pass
		try:
			if -1 != line.get_text().find('出版社'):
				storyPublish = line.nextSibling.replace(' ','').replace('\n','')
		except:
			pass
		try:
			if -1 != line.get_text().find('出版年'):
				storyDate = line.nextSibling.replace(' ','').replace('\n','')
		except:
			pass
		try:
			if -1 != line.get_text().find('页数'):
				storyPages = line.nextSibling.replace(' ','').replace('\n','')
		except:
			pass
		try:
			if -1 != line.get_text().find('定价'):
				storyPrices = line.nextSibling.replace(' ','').replace('\n','')
		except:
			pass
		try:
			if -1 != line.get_text().find('装帧'):
				storyGetUp = line.nextSibling.replace(' ','').replace('\n','')
		except:
			pass
		try:
			if -1 != line.get_text().find('丛书'):
				storyTotleName = line.nextSibling.nextSibling.get_text().replace(' ','').replace('\n','')
		except:
			pass		
		try:
			if -1 != line.get_text().find('ISBN'):
				storyISBN = line.nextSibling.replace(' ','').replace('\n','')
		except:
			pass
	print('书名:%s'%storyName)
	print('作者:%s'%storyAuthor)
	print('出版社:%s'%storyPublish)
	print('出版年:%s'%storyDate)
	print('页数:%s'%storyPages)
	print('定价:%s'%storyPrices)
	print('装帧:%s'%storyGetUp)
	print('丛书:%s'%storyTotleName)
	print('ISBN:%s'%storyISBN)
	return (storyName,storyAuthor,storyPublish,storyDate,storyPages,storyPrices,storyGetUp,storyTotleName,storyISBN)
def getAllInfo(url,start):
	htmlTree = getHtmlTree(url)
	try:
		ul = htmlTree.find('ul','subject-list')
		liList = ul.findAll('li')
	except:
		print('已经到达尾页！')
		return -1
	count = 0
	for line in liList:
		print('count = %d'%(start+count))
		count = count + 1
		flag = writeJudge('story.xlsx',start+count)
		if flag:
			continue
		try:
			imgTag = line.find('img')
			storyImgUrl = imgTag['src']
		except:
			print('没有找到封面！')
			storyImgUrl = 'NA'
		info = line.find('div',class_ = 'info')		
		storyDes = info.h2.a
		storyDesUrl = storyDes['href']
		storyList = ''
		(storyName,storyAuthor,storyPublish,storyDate,storyPages,storyPrices,storyGetUp,storyTotleName,storyISBN) = getKeyWord(storyDesUrl)
		try:
			storyCommit = line.find('span','rating_nums').text
			print('豆瓣评分:%s'%storyCommit)
		except:
			print('没有豆瓣评分！')
			storyCommit = ''
		try:
			remark = line.find('span','pl').get_text().replace(' ','').replace('\n','')
			storyName = info.h2.a.get_text()
		except:
			print('没有找到书名！')
			storyName = ''
		# pub = info.find('div','pub').get_text().replace(' ','').replace('\n','')
		try:
			storyDesIntro = line.find('p').text
		except:
			print('没有找到简述!')
			storyDesIntro = 'NA'
		else:
			print('简述:%s'%storyDesIntro)
		try:
			storyBuyIndex = line.find('span','buy-info')
			if None != storyBuyIndex:
				storyBuyTag = storyBuyIndex.a
				storyBuyLink = storyBuyTag['href']
				print('购买链接:%s'%storyBuyLink)
		except:
			print('没有找到购买链接！')
		else:
			storyBuyLink = ''
		storyList = [storyName,storyAuthor,storyPublish,storyDate,storyPages,storyPrices,storyGetUp,storyTotleName,storyISBN,storyCommit,storyDesIntro,storyImgUrl,storyBuyLink]
		writeExcel('story.xlsx',storyList,count+start)
url = 'https://book.douban.com/tag/%E5%A5%87%E5%B9%BB?start=20&type=T'
urlHead = 'https://book.douban.com/tag/%E5%A5%87%E5%B9%BB?start='
# urlHead = 'https://book.douban.com/subject/'
if __name__ == '__main__':
	step = 20
	for i in range(0,50):
		url = urlHead + str(step * i) + '&type=T'
		getAllInfo(url,step * i)




# https://book.douban.com/tag/%E5%A5%87%E5%B9%BB?start=20&type=T