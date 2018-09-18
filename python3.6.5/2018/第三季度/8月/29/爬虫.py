#!/usr/bin/env python
#coding=utf-8
#__author__ = 'Administrator'
import os
import sys
import re
from bs4 import BeautifulSoup
import requests
from lxml import etree

def GetHtmlEtree(url):
    response = requests.get(url = url)
    response.encoding = 'utf-8'
    content = response.content
    html = etree.HTML(content)
    return html

def GetDict(url):
    html = GetHtmlEtree(url)
    href = html.xpath('//*[@id="info"]/div[1]/ul/li[*]/a/@href')
    href = sorted(list(set(href)))
    chapterList = [url+line for line in href]
    # print(x)
    storyName = html.xpath('//*[@id="info"]/div[1]/div[2]/h1/text()')[0]
    print(storyName,type(storyName))
    return storyName,chapterList
    # print(len(href),href)

def GetKeyInfo(url):
    html = GetHtmlEtree(url)
    chapterName = html.xpath('//*[@id="info"]/div[1]/h1/text()')[0]
    content = html.xpath('//*[@id="content1"]/text()')
    tmp = ''
    for line in content:
        tmp = tmp + line
    content = tmp.replace('\r','') + '\n'
    print(chapterName)
    return (chapterName,content)

def SaveFile(filename,content):
    with open(filename,'a+',encoding='utf-8') as f:
        f.write(content)
        f.close()

if __name__ == "__main__":
    for x in range(8646,8647):
        tmp = 'https://www.qisuu.la/du/8/'+str(x)+'/'
        url=tmp
        storyName,chapterList = GetDict(url)
        for line in chapterList:
            (chapterName,content) = GetKeyInfo(line)
            tmp = str(chapterName) + content
            SaveFile(storyName + '.txt',tmp)
            # https://www.qisuu.la/du/8/8646/