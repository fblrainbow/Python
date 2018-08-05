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
url_totle = 'http://www.f96.net/11/11327/'
Domain = 'http://www.f96.net/'
Classify = 11
# Number = 11631   #盘龙
Number = 11327   #圣墟
# print(type(Classify))
def GetHtmlCode(url):
	delay = 5
	while True:
		response = requests.get(url = url)
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
url_tmp = 'http://www.f96.net/11/11327/3800188.html'
def GetChapterKeyContent(url):
	HtmlTree = GetHtmlTree(url)
	try:
		ContentTitle = HtmlTree.h1.text
		ContentTag = HtmlTree.find('div',id = 'htmlContent').text
		ChapterContent = ContentTitle + ContentTag
		return ChapterContent
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
	cmd.append('move ' + '*.txt ' + Classify + '\\' + Number)
	cmd.append('CombineChapter.bat ' + Classify + ' ' + Number + ' '+ StoryName)
	for line in cmd:
		print(line)
		os.system(line)

class Story(object):
	def __init__(self,Domain,Classify,Number):
		if False == isinstance(Domain,str):
			print('Domain type Error!')
			exit
		if False == isinstance(Classify,int):
			print('Classify type Error!')
			exit
		if False == isinstance(Number,int):
			print('Number type Error!')
			exit
		if '/' != Domain[-1]:
			self.url = Domain + '/' + str(Classify) + '/' + str(Number) + '/'
		else:
			self.url = Domain + str(Classify) + '/' + str(Number) + '/'
		self.miss = 0
 
	def GetChapterDict(self):
		HtmlTree = GetHtmlTree(self.url)
		StoryName = HtmlTree.h1.a.text.replace(' ','')

		self.StoryName = StoryName
		UlTag = HtmlTree.find('ul',class_='mulu_list')

		LiTagList = UlTag.find_all('a')

		ChapterDict ={}
		for line in LiTagList:
			ChapterHref = self.url + line['href'].split('/')[-1]
			ChapterTitle = line['title']
			ChapterDict[ChapterHref] = ChapterTitle
		self.dict = ChapterDict
	def GetChapterContent(self):
		for u,t in self.dict.items():
			ChapterKeyContent = GetChapterKeyContent(u)
			if False == ChapterKeyContent:
				self.miss = self.miss + 1
				print(self.miss)
			else:
				SaveChapter(t,ChapterKeyContent)
			# break
s1 = Story(Domain,Classify,Number)
s1.GetChapterDict()
s1.GetChapterContent()
CombineChapter(Classify,Number,'Combine')
