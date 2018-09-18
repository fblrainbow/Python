#!/usr/bin/env python
#coding=utf-8
#__author__ = 'Administrator'


from html.parser import HTMLParser
from lxml import etree
import requests,sys,io
import time
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

def GetHtmlElemt(url):
    response = requests.get(url = url)
    response.encoding = "utf-8"

    print(response.apparent_encoding)
    if response.status_code != 200:
        time.sleep(10)
        print(response.status_code)
        # GetHtmlElemt(url)
    # print(str(response.content.decode('utf-8',"ignore")))
    htmlElemt = etree.HTML(response.content)
    return htmlElemt

def GetKeyInfo(url):
    htmlElemt = GetHtmlElemt(url)
    storyName = htmlElemt.xpath('/html/body/div[4]/div[2]/h2/text()')
    chapterLinkList = htmlElemt.xpath('/html/body/div[5]/dl/dd/a/@href')
    # chapterLinkList = [x.replace(' ','').replace('\n','') for x in chapterLinkList]
    # chapterLinkList = sorted(list(set(chapterLinkList)))
    print(storyName)
    print(chapterLinkList)
    return storyName,chapterLinkList

def SaveFile(storyName,content,mode = 'a+',code = 'gbk'):
    with open(storyName,mode = mode,encoding = code) as f:
        f.write(content)
        f.close()

def GetChapterContent(url):
    htmlElemt1 = GetHtmlElemt(url)
    content1 = htmlElemt1.xpath('//*[@id="wrapper"]/div[5]/div/div[2]/h1/text()')
    chapterName = htmlElemt1.xpath('//*[@id="content"]/text()')
    print(type(url))
    tmpurl = url[0:-5] + '_2.html'
    print(chapterName,tmpurl)
    # tmp = ''
    # for line in content:
    #     tmp = tmp + line
    # content = tmp.replace('\r\n','').replace('\xa0','') + '\n'
    # return content

if __name__ == '__main__':
    url = 'http://www.biqiuge.com/book/1/'
    storyName,chapterLinkList = GetKeyInfo(url)
    for index,line in enumerate(chapterLinkList):
        GetChapterContent(line)
        break
        print(content)
        SaveFile(storyName,content)

        print('已下载%.2f%%'%((index+1)/len(chapterLinkList) * 100))


