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

url = 'https://jobs.51job.com/guangzhou/103690520.html?s=01&t=0'

def GetHtmlCode(url):
	response = requests.get(url=url,cookies=cookies,headers=headers)
	if 200 != response.status_code:
		print('请求失败！')

	response.encoding = 'gbk'
	HtmlCode = response.text
	print(HtmlCode)
	return HtmlCode

# def GetKeyInfo(url):
# 	HtmlCode = GetHtmlCode(url)
# 	HtmlTree = BeautifulSoup(HtmlCode,'html.parser')

GetHtmlCode(url)