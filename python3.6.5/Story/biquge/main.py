#coding:utf-8

import requests
import json
import pymysql
import os
import sys
import time
from lxml import etree
import path

def dataDeal(content):
    # 打开数据库连接
    db = pymysql.connect(host = 'localhost',user = 'root',passwd ='FBLATPX520@',db = 'cfets',charset='utf8' )

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    try:
        cursor.execute(content)
        print(cursor.fetchall())
        db.commit()
        db.close()
    except:
        db.close()
def saveFile(filename,content):
    try:
        with open(filename,"a+",encoding='utf-8') as f:
            f.write(content)
            f.close()
    except:
        pass
def readFile(filename):
    with open(filename,"r") as f:
        content = f.read()
        return content
def getCode(url):
    response = requests.get(url = url)
    return response.text
def getHtmlStruct(url):
    response = requests.get(url = url)
    return etree.HTML(response.text)
def get_FileSize(filePath):
    fsize = os.path.getsize(filePath)
    fsize = fsize/float(1024*1024)
    return round(fsize,4)

class Story(object):
    def __init__(self,url):
        self.url = url
    def getHtmlList(self):
        code = getCode(self.url)
        htmlStruct = etree.HTML(code)
        storyName = htmlStruct.xpath('//*[@id="info"]/h1/text()')
        self.storyName = ''.join(storyName) + '.txt'
        cmd = 'del ' + self.storyName
        os.system(cmd)
        #//*[@id="list"]/dl/dd[10]/a
        elementList = [int(line.split("/")[-1][0:-5]) for line in htmlStruct.xpath('//*[@id="list"]/dl/dd/a/@href')]
        uniqueElementList = list(set(elementList))
        sortedElementList = sorted(uniqueElementList)
        hrefElementList = [self.url + str(line) + '.html' for line in sortedElementList]
        self.hrefElementList = hrefElementList
        return hrefElementList
    def getStory(self):
        storyLen = len(self.hrefElementList)
        for index,line in enumerate(self.hrefElementList):
            time.sleep(0.5)
            chapterHtmlStruct = getHtmlStruct(line)
            #//*[@id="wrapper"]/div[4]/div/div[2]/h1  /html/body/div/div[4]/div/div[2]/h1    /html/body/div/div[4]/div/div[5]/p[1]
            chapterName = (chapterHtmlStruct.xpath('/html/head/title/text()'))[0]
            chapterContent_1 = [line.replace('\u3000','')  for line in chapterHtmlStruct.xpath('//*[@id="content"]/p/text()') if line != ';' and line != "\n"]
            chapterContent = chapterName.strip() + '\n' + '\n'.join(chapterContent_1) + "\n"
            saveFile(self.storyName,chapterContent)
            printStr = "保存进度{0:.2f}%\t文件大小{1:.3f}M\t章节名：{2:10s}\t小说名：{3:10s}\t链接：{4}\n".format((index+1)/storyLen * 100,get_FileSize(self.storyName),chapterName,self.storyName,self.url)
            saveFile("story.log",printStr)
            if (index + 1) % 20 == 0:
                print(printStr)

if __name__ == "__main__":
    # url = "https://www.biquge5200.cc/0_916/"   #总网站
    cmd = 'del story.log'
    os.system(cmd)
    for urlIndex in range(1958,1959,1):
        url = 'http://www.biquyun.com/1_' + str(urlIndex) + '/'
        saveFile("current.txt",'开始：' + time.ctime() + '\t'  + url + '\n')
        bqgStory = Story(url)
        bqgStory.getHtmlList()
        bqgStory.getStory()
        saveFile("current.txt",'结束' + time.ctime() + '\t'  + url + '\n\n\n')