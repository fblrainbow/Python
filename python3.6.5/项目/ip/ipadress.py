#coding:utf-8
import re 
import os
import sys 
from bs4 import BeautifulSoup 
from urllib import request 
import ssl 
import socket 
import time
def getHtmlCode(url): 
	page = request.urlopen(url)
	html = page.read() 
	print(html)
	htmlTree = BeautifulSoup(html,'html.parser') 
	return htmlTree 
#return htmlTree.prettify() 
def getKeyContent(url): 
	htmlTree = getHtmlCode(url) 
def parserCaption(url): 
	htmlTree = getHtmlCode(url) 
def saveFile(fileName,content):
	with open(fileName,"a",encoding='utf-8') as f:
		f.write(content)
		f.close()
if __name__ == "__main__":
	# url = 'http://www.chinamoney.com.cn/ags/ms/cm-u-bk-shibor/Ifcc?lang=CN&cfgItemType=71' 
	dns = "www.chinamoney.com.cn"
	while True:
		time.sleep(10)
		ip = socket.gethostbyname(dns) 
		string = "IP:" + ip + "\t" + "Time" + time.asctime() + "\n"
		saveFile("IP.txt",string)
		print(string)