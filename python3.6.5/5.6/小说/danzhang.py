#coding:utf-8

import re
import os
import sys
from bs4 import BeautifulSoup
from urllib import request
import ssl
url = 'http://www.biqiuge.com/book/4772/'
url = 'https://www.qu.la/book/1/'
url = 'http://www.biqiuge.com/book/1/3.html'

def getHtmlCode(url):
    page = request.urlopen(url)
    html = page.read()  
    htmlTree = BeautifulSoup(html,'html.parser')
    return htmlTree
    # return htmlTree.prettify()
def getKeyContent(url):
	htmlTree = getHtmlCode(url)
	# print(htmlTree)
	chapterName = htmlTree.h1.get_text()  #章节名
	tmp = htmlTree.find_all('div',id='content')
	tmp = tmp[0].contents[1].get_text()
	f = open('tmp.txt','w+',encoding='utf-8')
	f.write(tmp)
	f.close()
getKeyContent(url)
# f = open('tmp.txt','a',encoding = 'utf-8')
# for line in f.readlines():
#     print(line)

# f.close()
    
	