#!/usr/bin/env python3
#coding:utf-8


import re
import os
import sys
import requests
from bs4 import BeautifulSoup

headers = {
	'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4882.400 QQBrowser/9.7.13059.400'
}
url = 'https://book.douban.com/subject/3359946/'
url = 'https://book.douban.com/subject/26853356/'
# url = 'https://book.douban.com/subject/27035185/'
# url = 'https://book.douban.com/subject/22227388/'
def getHtmlTree(url):
	tmp = requests.get(url,headers = headers)
	text = tmp.text
	htmlTree = BeautifulSoup(text,'html.parser')
	return htmlTree

def getKeyWord(url):
	htmlTree = getHtmlTree(url)
	storyName = htmlTree.find('span',property="v:itemreviewed").get_text()
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
		if -1 != line.get_text().find('出版社'):
			storyPublish = line.nextSibling.replace(' ','').replace('\n','')
		if -1 != line.get_text().find('出版年'):
			storyDate = line.nextSibling.replace(' ','').replace('\n','')
		if -1 != line.get_text().find('页数'):
			storyPages = line.nextSibling.replace(' ','').replace('\n','')
		if -1 != line.get_text().find('定价'):
			storyPrices = line.nextSibling.replace(' ','').replace('\n','')
		if -1 != line.get_text().find('装帧'):
			storyGetUp = line.nextSibling.replace(' ','').replace('\n','')
		if -1 != line.get_text().find('丛书'):
			storyTotleName = line.nextSibling.nextSibling.get_text().replace(' ','').replace('\n','')
		if -1 != line.get_text().find('ISBN'):
			storyISBN = line.nextSibling.replace(' ','').replace('\n','')
	if '' == storyName:
		storyName = 'Unknow'
	if '' == storyAuthor:
		storyAuthor = 'Unknow'	
	if '' == storyPublish:
		storyPublish = 'Unknow'
	if '' == storyDate:
		storyDate = '1970-01-01'
	if '' == storyPages:
		storyPages = -1
	if '' == storyGetUp:
		storyGetUp = 'Unknow'
	if '' == storyTotleName:
		storyTotleName = ''
	if '' == storyISBN:
		storyISBN = -1
	print('书名:%s'%storyName)
	print('作者:%s'%storyAuthor)
	print('出版社:%s'%storyPublish)
	print('出版年:%s'%storyDate)
	print('页数:%s'%storyPages)
	print('装帧:%s'%storyGetUp)
	print('丛书:%s'%storyTotleName)
	print('ISBN:%s'%storyISBN)

urlHead = 'https://book.douban.com/subject/'
if __name__ == '__main__':
	urlStart = 27035100
	urlEnd = 27035190
	for index in range(urlStart,urlEnd):
		url_tmp = urlHead + str(index) + '/'
		print('index = %d'%index)
		getKeyWord(url_tmp)
		print('----------')
