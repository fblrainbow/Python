#!/usr/bin/env python3
#coding=utf-8

import requests
from bs4 import BeautifulSoup

# 面试题网址
url = 'https://news.html5.qq.com/share/7543188774165644438?url=http%3A%2F%2Fkuaibao.qq.com%2Fs%2F20180624A15HUO00&ch=060000&qbredirect=&share=true&sc_id=YdSw6lC'

class text():
	# get到网页源代码，用BeautifulSoup解析成tree结构
	def __init__(self,url):
		response = requests.get(url)
		tmp = response.text
		htmltree = BeautifulSoup(tmp,'html.parser')
		self.htmltree = htmltree

	# 得到关键信息
	def getkeyinfo(self):
		title = self.htmltree.h1.get_text()
		self.title = title + '.txt'
		content = self.htmltree.find('article')
		content = content.find_all('span')
		content = [x.get_text() for x in content]
		self.content = content

	# 保存文本信息
	def savefile(self):
		with open(self.title,'w+',encoding = 'utf-8') as f:
			for i in self.content:
				f.write(i + '\n')
		f.close()

t = text(url)
t.getkeyinfo()
t.savefile()