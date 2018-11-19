#coding:utf-8

import requests
import json
import pymysql
import os
import sys
import time,datetime
from lxml import etree
import path

def dataDeal(content):
    # 打开数据库连接
    db = pymysql.connect(host = 'localhost',user = 'root',passwd ='FBLATPX520@',db = 'csdn',charset='utf8' )

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    cursor.execute(content)
    db.commit()
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
        name = htmlStruct.xpath('/html/head/meta[2]/@content') #//*[@id="csdnc-bloglevel-6"]
        level = htmlStruct.xpath('/html/body/div[1]/div[1]/div/div[2]/div/ul/li[1]/span/svg/use/text()')
        visitors = htmlStruct.xpath('/html/body/div[1]/div[1]/div/div[2]/div/ul/li[2]/span/text()')
        create = htmlStruct.xpath('/html/body/div[1]/div[1]/div/div[2]/div/ul/li[3]/span/text()')
        transfer = htmlStruct.xpath('/html/body/div[1]/div[1]/div/div[2]/div/ul/li[4]/span/text()')
        fans = htmlStruct.xpath('/html/body/div[1]/div[2]/div[3]/ul/li[1]/em/text()')
        rank = htmlStruct.xpath('/html/body/div[1]/div[1]/div/div[2]/div/ul/li[5]/span/text()')
        remarks = htmlStruct.xpath('/html/body/div[1]/div[1]/div/div[2]/div/ul/li[6]/span/text()')
        like = htmlStruct.xpath('/html/body/div[1]/div[1]/div/div[2]/div/ul/li[7]/span/text()')
        self.name = name
        print(name,level,visitors,create,transfer,rank,remarks,fans,like)
        #INSERT INTO `csdn`.`csdn` (`name`, `url`, `createChapter`, `fans`, `like`, `remark`, `level`, `visitors`, `score`, `rank`) VALUES ('A', 'A', '123', '12', '23', '123', '123', '123', '123', '123');

        # stringCSDN = "insert into csdn( `url`, `createChapter`, `fans`, `likes`, `remark`, `levels`, `visitors`, `score`, `rank`) VALUES ( `%s`, `%s`, `%s`, `%s`, `%s`,`%s`, `%s`, `%s`, `%s`)"%(self.url,create[0],fans[0],like[0],remarks[0],6,visitors[0], 0,rank[0])
        # UPDATE `csdn`.`csdn` SET `csdnname`='A', `url`='A', `createChapter`='123', `fans`='12', `likes`='23', `remark`='123', `levels`='123', `visitors`='123', `score`='123', `rank`='123' WHERE (`csdnname`='A') AND (`url`='A') AND (`createChapter`='123') AND (`fans`='12') AND (`likes`='23') AND (`remark`='123') AND (`levels`='123') AND (`visitors`='123') AND (`score`='123') AND (`rank`='123') LIMIT 1;
        #INSERT INTO `csdn`.`csdn` (`csdnname`, `url`, `createChapter`, `fans`, `likes`, `remark`, `levels`, `visitors`, `score`, `rank`) VALUES ('A', 'A', '123', '12', '23', '123', '123', '123', '123', '123');
        #INSERT INTO `csdn`.`csdn` (`url`, `createChapter`, `fans`, `likes`, `remark`, `levels`, `visitors`, `score`, `rank`) VALUES ('A', '123', '12', '23', '123', '123', '123', '123', '123');
        strTime = datetime.datetime.now().strftime("%Y%m%d-%H:%M:%S")
        stringCSDN = "INSERT INTO `csdn`.`csdn` (`csdnname`, `url`, `createChapter`, `fans`, `likes`, `remark`, `levels`, `visitors`, `score`, `rank`,`dataTime`) VALUES ( '%s','%s', '%s', '%s', '%s', '%s','%s', '%s', '%s', '%s','%s');" %(name[0],self.url,create[0],fans[0],like[0],remarks[0],6,visitors[0], 0,rank[0],strTime)

        dataDeal(stringCSDN)
if __name__ == "__main__":
    # url = "https://blog.csdn.net/qq_37608398/article/details/83480197"   #总网站
    url = "https://me.csdn.net/qq_37608398"   #总网站

    myCSDN = CSDN(url)
    myCSDN.getHtmlList()