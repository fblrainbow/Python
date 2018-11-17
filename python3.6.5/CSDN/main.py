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
