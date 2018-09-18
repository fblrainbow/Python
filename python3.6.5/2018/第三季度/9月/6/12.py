
#!/usr/bin/env python
#coding=utf-8
#__author__ = 'Administrator'
#coding:utf-8

import re
import os
import sys
from bs4 import BeautifulSoup
from urllib import request
import ssl
url = 'http://www.biqiuge.com/book/4772/'
url = 'https://www.qu.la/book/1/'
url = 'http://www.biqiuge.com/book/1/'

def getHtmlCode(url):
    page = request.urlopen(url)
    html = page.read()
    htmlTree = BeautifulSoup(html,'html.parser')
    return htmlTree
    #return htmlTree.prettify()
def getKeyContent(url):
    htmlTree = getHtmlCode(url)

def parserCaption(url):
    htmlTree = getHtmlCode(url)
    storyName = htmlTree.h1.get_text() + '.txt'

    print('小说名:',storyName)
    aList = htmlTree.find_all('a',href=re.compile('(\d)*.html'))  #aList是一个标签类型的列表，class = Tag 写入文件之前需要转化为str
    # print(int(aList[1]['href'][0:-5]))
    aDealList = []
    for line in aList:
        # line['href'] = url + line['href']
        # print(line['href'])
        chapter = int(line['href'][0:-5])
        if chapter not in aDealList:    #去重
            aDealList.append(chapter)
    aDealList.sort()    #排序
    # print(aDealList)
    # print(len(aDealList))
    # aDealList = str(aDealList)
    urlList = []
    for line in aDealList:
        line = url + str(line) + '.html'
        urlList.append(line)
    # print(urlList)
    print(urlList)
    return (storyName,urlList)
def parserChapter(url):
    htmlTree = getHtmlCode(url)
    title = htmlTree.h1.get_text()  #章节名
    content = htmlTree.find_all('div',id = 'content')
    content = content[0].contents[1].get_text()
    return (title,content)
def main(url):
    (storyName,urlList) = parserCaption(url)
    flag = True
    cmd = 'del ' + storyName
    os.system(cmd)
    cmd = 'cls'
    count = 1
    for url_alone in urlList:
        percent = count / len(urlList) * 100
        print('%s 下载进度 %0.2f %%'%(storyName,percent))
        f = open(storyName,'a+',encoding = 'utf-8')
        (title,content) = parserChapter(url_alone)
        tmp = title + '\n' + content
        f.write(tmp)
        f.close()
        count = count + 1

main(url)
