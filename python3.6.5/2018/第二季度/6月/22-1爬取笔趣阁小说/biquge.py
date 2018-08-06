#!/usr/bin/env python3
#coding:utf-8

import requests
from bs4 import BeautifulSoup
import os
import re
import sys
import json
import time

import datetime
from lxml import etree

# 书香阁
# url_totle = 'http://www.f96.net/11/11631/'
headers = {
	'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.5155.400 QQBrowser/9.7.13231.400'
}
cookies = {
	'Cookie':'UM_distinctid=164280145ca9d35-0b466517b9188d-354c7e51-1fa400-164280145da807; bookid=24868; chapterid=8680154; chaptername=%25u7B2C%25u4E8C%25u7AE0%2520%25u540E%25u6587%25u660E%25u65F6%25u4EE3; bcolor=; font=; size=; fontcolor=; width=; ASP.NET_SessionId=miy1tw45j1e2ir45kaepar55; m_uid=c96c79a4-0d6b-449d-8ae9-c535d0aa5708; member_username=fbl4869; CNZZDATA1261736110=527061289-1529674930-https%253A%252F%252Fwww.baidu.com%252F%7C1529674930; Hm_lvt_5ee23c2731c7127c7ad800272fdd85ba=1529679530; Hm_lpvt_5ee23c2731c7127c7ad800272fdd85ba=1529679954'
}

url_totle = 'https://www.qu.la/book/379/'
Domain = 'https://www.qu.la/'
Classify = 'book'
# Number = 11631   #盘龙
# Number = 24866   #圣墟
# print(type(Classify))
def GetHtmlCode(url):
	delay = 5
	while True:
		try:
			response = requests.get(url = url,cookies = cookies,headers = headers)
		except:
			continue
		if 200 == response.status_code:
			if 'ISO-8859-1' == response.encoding:
				response.encoding = 'gbk'
			return response.text
		else:
			print('请求失败，重新请求！')
			time.sleep(delay)
			delay = 2 * delay

def GetHtmlTree(url):
	HtmlCode = GetHtmlCode(url)
	HtmlTree = BeautifulSoup(HtmlCode,'html.parser')
	return HtmlTree

def GetChapterKeyContent(url):
	HtmlTree = GetHtmlTree(url)
	try:
		# ChapterContent = {}
		ContentTitle = HtmlTree.h1.text
		Content = HtmlTree.find('div',id = 'content').text
		return (ContentTitle,Content)
	except:
		return False

def SaveChapter(title,content):
	with open(title + '.txt','w',encoding='utf-8') as f:
		f.write(content)
		f.close()

def CombineChapter(Classify,Number,StoryName):
	Classify = str(Classify)
	Number = str(Number)
	cmd = []
	cmd.append('chcp 65001')
	cmd.append('mkdir ' + Classify + '\\' + Number)
	cmd.append('move /y ' + '*.txt ' + Classify + '\\' + Number)
	cmd.append('CombineChapter.bat ' + Classify + ' ' + Number + ' '+ StoryName)
	for line in cmd:
		print(line)
		os.system(line)

class Story(object):
	def __init__(self,Domain,Classify,Number):
		if False == isinstance(Domain,str):
			print('Domain type Error!')
			exit
		if False == isinstance(Classify,str):
			print('Classify type Error!')
			exit
		if False == isinstance(Number,int):
			print('Number type Error!')
			exit
		self.Domain = str(Domain)
		self.Classify = str(Classify)
		self.Number = str(Number)
		if '/' != Domain[-1]:
			self.url = Domain + '/' + str(Classify) + '/' + str(Number) + '/'
		else:
			self.url = Domain + str(Classify) + '/' + str(Number) + '/'
		self.miss = 0
 
	def GetChapterList(self):
		HtmlTree = GetHtmlTree(self.url)
		StoryName = HtmlTree.h1.text
		# print(StoryName)
		self.StoryName = StoryName
		UlTag = HtmlTree.find('dl')
		LiTagList = UlTag.find_all('a')
		# print(LiTagList)
		ChapterHrefList = []
		for line in LiTagList:
			ChapterHref = int(line['href'].split('/')[-1].split('.')[0])
			ChapterHrefList.append(ChapterHref)
		# self.dict = ChapterDict
		# print(len(ChapterHrefList))
		ChapterHrefList = list(set(ChapterHrefList))
		# print(ChapterHrefList)
		ChapterHrefList.sort()
		tmp = []
		for line in ChapterHrefList:
			line = self.url + str(line) + '.html'
			tmp.append(line)
		# print(tmp)
		self.ChapterHrefList = tmp

	def GetChapterContent(self):
		for line in self.ChapterHrefList:
			ChapterKeyContent = GetChapterKeyContent(line)
			print(ChapterKeyContent[0])
			SaveChapter(ChapterKeyContent[0].replace(' ','-').replace('?','').replace('!','').replace('：',''),ChapterKeyContent[0] + ChapterKeyContent[1])
	def ChapterCombine(self):
		CombineChapter(self.Classify,self.Number,'Combine')
for Number in range(24504,24855,1):
	s1 = Story(Domain,Classify,Number)
	s1.GetChapterList()
	s1.GetChapterContent()
	s1.ChapterCombine()
	# os.system('del /q /s *.txt')
	
