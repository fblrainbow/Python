#!/usr/bin/env python
#coding:utf-8

import re
import time
import requests
from bs4 import BeautifulSoup

def get_html(href):
		response = requests.get(url = href)
		response.encoding = 'gbk'	
		html_tree = BeautifulSoup(response.text,'html.parser')
		return html_tree
def save_file(story_name,chapter_name,chapter_content):
	f = open(story_name + '.txt','a+',encoding = 'utf-8')
	f.write('\n' + chapter_name + '\n' + chapter_content)
	f.close()

class get_info():
	def __init__(self,url,cookies,headers):
		self.url = url
		self.cookies = cookies
		self.headers = headers

	def get_html_tree(self):
		response = requests.get(url = self.url,cookies = self.cookies,headers = self.headers)
		# print(dir(response))
		'''
		['__attrs__', '__bool__', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__enter__', '__eq__', 
		 '__exit__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', 
		 '__iter__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__nonzero__', 
		 '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 
		 '_content', '_content_consumed', '_next', 'apparent_encoding', 'close', 'connection', 'content', 'cookies', 'elapsed', 'encoding', 'headers', 
		 'history', 'is_permanent_redirect', 'is_redirect', 'iter_content', 'iter_lines', 'json', 'links', 'next', 'ok', 'raise_for_status', 
		 'raw', 'reason', 'request', 'status_code', 'text', 'url']
		'''
		# print(response.apparent_encoding,)
		# response.encoding = 'GB2312'
		response.encoding = 'gbk'	
		html_tree = BeautifulSoup(response.text,'html.parser')
		self.html_tree = html_tree
	def get_key_info(self):
		tmp = self.html_tree.find('span',id = 'htmldhshuming')
		self.story_name = tmp.a.get_text()
		tmp =self.html_tree.find('div',style = 'min-height:420px;')
		tmp_list = tmp.find_all('a')
		# print(tmp_list,len(tmp_list))
		url_head = '/'.join(self.url.split('/')[0:-1]) + '/'
		self.chapter_map = {}
		for x in tmp_list:
			href = x['href']
			chapter = x.get_text()
			self.chapter_map[url_head + href] = chapter
		# print(self.chapter_map)
	def get_chapter_content(self):
		for href,chapter_name in self.chapter_map.items():
			chapter_html_tree = get_html(href)
			chapter_html_content = chapter_html_tree.find('div',id = 'htmlContent').get_text().replace('\n','').replace('\r','').replace('(免费全本小说YZNN．ＣＯm)','')\
			.replace('作者的话:    新书上传,更新稳定,亲们多支持啊。    ,！    全本欢迎您！ t1706231537全本小说网欢迎您！WWW.YZNN.COM T1706231537','')\
			.replace('(免费全本小说щщщ.yznn.com)','')
			print(chapter_name,href)
			# if isExist(self.story_name,chapter_name):
			# file_save(self.story_name,chapter_name,chapter_html_content)
			save_file(self.story_name,chapter_name,chapter_html_content)
			


