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
    db = pymysql.connect(host = 'localhost',user = 'root',passwd ='FBLATPX520@',db = 'csdn',charset='utf8' )

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
    with open(filename,"a+",encoding='utf-8') as f:
        f.write(content)
        f.close()
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

class CSDN(object):
    def __init__(self,url):
        self.url = url
    def getHtmlList(self):
        code = getCode(self.url)
        htmlStruct = etree.HTML(code)
        name = htmlStruct.xpath('/html/head/meta[2]/@content')
        level = htmlStruct.xpath('/html/body/div[2]/div[1]/div/div[2]/div/ul/li[1]/span/svg/use/text()')
        visitors = htmlStruct.xpath('/html/body/div[1]/div[1]/div/div[2]/div/ul/li[2]/span/text()')
        create = htmlStruct.xpath('/html/body/div[1]/div[1]/div/div[2]/div/ul/li[3]/span/text()')
        transfer = htmlStruct.xpath('/html/body/div[1]/div[1]/div/div[2]/div/ul/li[4]/span/text()')
        rank = htmlStruct.xpath('/html/body/div[1]/div[1]/div/div[2]/div/ul/li[5]/span/text()')
        remarks = htmlStruct.xpath('/html/body/div[1]/div[1]/div/div[2]/div/ul/li[6]/span/text()')
        print(name,level,visitors,create,transfer,rank,remarks)
        stringCSDN = "re"

if __name__ == "__main__":
    # url = "https://blog.csdn.net/qq_37608398/article/details/83480197"   #总网站
    url = "https://me.csdn.net/qq_37608398"   #总网站

    myCSDN = CSDN(url)
    myCSDN.getHtmlList()
