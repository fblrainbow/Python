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



cookies = {
	'Cookie':'partner=www_baidu_com; guid=15295726858410610050; _ujz=MTA3OTgyMzQwMA%3D%3D; slife=lastlogindate%3D20180621%26%7C%26; ps=us%3DDTRQMwZnV38GZl0wVi0HMgU%252BBilbb1IyBzBUeg02AjcBOwZkBmECM1Y1AGsLbgM1VmZWYQA0UHkFYlZKWwlTAw1k%26%7C%26needv%3D0; 51job=cuid%3D107982340%26%7C%26cusername%3Dfbl1228%26%7C%26cpassword%3D%26%7C%26cname%3D%25B7%25B6%25B1%25FE%25C1%25D6%26%7C%26cemail%3D18271676080%2540163.com%26%7C%26cemailstatus%3D3%26%7C%26cnickname%3D%26%7C%26ccry%3D.05ZIADS9uJGg%26%7C%26cconfirmkey%3D18P0996j19O4c%26%7C%26cresumeids%3D.0iX78O5vOycg%257C.04Da8BF2ugTU%257C%26%7C%26cautologin%3D1%26%7C%26cenglish%3D0%26%7C%26sex%3D0%26%7C%26cnamekey%3D18lfsbMKTxs6A%26%7C%26to%3DXGVVPgdiU2xXPgtlC21QZwMwA35TM1JlXTdRMgE5BDYMPFdwAmFXZFYxDGEDZ1VmBj0EMlJmUzM%253D%26%7C%26'
}
headers = {
	'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.5155.400 QQBrowser/9.7.13231.400'
}

url = 'https://search.51job.com/list/030200,000000,0000,01,3,07,%2B,2,1.html?lang=c&stype=1&postchannel=0000&workyear=02&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=4&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='

def GetHtmlCode(url):
	response = requests.get(url=url,cookies=cookies,headers=headers)
	if 200 != response.status_code:
		print('请求失败！')
	# print(dir(response))
	# print(response.encoding)
	response.encoding = 'gbk'
	HtmlCode = response.text
	# print(HtmlCode)
	return HtmlCode

def GetKeyInfo(url):
	HtmlCode = GetHtmlCode(url)
	HtmlTree = BeautifulSoup(HtmlCode,'html.parser')
	tmp = HtmlTree.find('div',class_='dw_table')
	TitleHtml = tmp.find('div',class_='el title')
	TitleHtml_tmp = TitleHtml.find_all('span')
	t1 = TitleHtml_tmp[0].text
	t2 = TitleHtml_tmp[1].text
	t3 = TitleHtml_tmp[2].text
	t4 = TitleHtml_tmp[3].text
	t5 = TitleHtml_tmp[4].text

	t1_list_tmp = tmp.find_all('p',class_='t1')
	t1_list = []
	t6_list = []
	for line in t1_list_tmp:
		href = line.a['href']
		t6_list.append(href)
		line = line.a.text.replace(' ','').replace('\r\n','')
		t1_list.append(line)

	t2_list_tmp = tmp.find_all('span',class_='t2')
	t2_list = []
	for line in t2_list_tmp:
		try:
			line = line.a['title']
			t2_list.append(line)
		except:
			pass

	t3_list_tmp = tmp.find_all('span',class_='t3')
	t3_list = []
	for line in t3_list_tmp:
		try:
			line = line.text
			t3_list.append(line)
		except:
			pass

	t4_list_tmp = tmp.find_all('span',class_='t4')
	t4_list = []
	for line in t4_list_tmp:
		try:
			line = line.text
			t4_list.append(line)
		except:
			pass

	t5_list_tmp = tmp.find_all('span',class_='t5')
	t5_list = []
	for line in t5_list_tmp:
		try:
			line = line.text
			t5_list.append(line)
		except:
			pass
	t6 = '网址'
	print(len(t1_list),len(t2_list),len(t3_list),len(t4_list),len(t5_list))
	dict_totle = {}

	for line in range(0,len(t1_list)):
		tmp = {}
		tmp[t1] = t1_list[line]
		tmp[t2] = t2_list[line]
		tmp[t3] = t3_list[line+1]
		tmp[t4] = t4_list[line+1]
		tmp[t5] = t5_list[line+1]
		tmp[t6] = t6_list[line]
		dict_totle[line+1] = tmp
	print(dict_totle)
	# for count in range(0,len(t1_list)):
	# 	tmpString = t1 + ':' t1_list[count] + '\n' + t2 + ':' t2_list[0] + '\n' + 

	# print(list_totle)
GetKeyInfo(url)