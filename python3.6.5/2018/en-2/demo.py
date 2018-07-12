#!/usr/bin/env python3
#coding:utf-8
import pymysql
import re
import os
import requests
import time
from bs4 import BeautifulSoup

# 打开数据库连接
db = pymysql.connect(host = 'localhost',user = 'root',passwd ='FBLATPX520@',db = 'fbl' )
 
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
 
# 使用 execute()  方法执行 SQL 查询 
# cursor.execute("SELECT VERSION()")
cmd_list = []

# cmd_list.append('show tables;')

# cmd_list.append('insert into hunpo(title,url) values("adfsf","qml");')
# cmd_list.append('insert into hunpo(title,url) values("qml","fbl");')
cookie = {
	'Cookie':'fikker-CfIR-orCF=atKFEJAbgR7lOvGVcrK0OlLVcxuhS2mP; fikker-CfIR-orCF=atKFEJAbgR7lOvGVcrK0OlLVcxuhS2mP; Hm_lvt_8e60c441f1fbb9ff966b1c6404d6fd58=1528626517,1528656567,1528730510; Hm_lpvt_8e60c441f1fbb9ff966b1c6404d6fd58=1528730536'
}
header = {
	'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.5155.400 QQBrowser/9.7.13231.400'
} 

cmd_list.append('select * from hunpo;')

def GetHtmlCode(url):
	response = requests.get(url = url,cookies = cookie,headers = header)
	# print(type(response.status_code))
	delay = 10
	while 503 == response.status_code:
		print('服务器压力太大了!')
		time.sleep(delay)
		delay = delay + 10
		print(delay)
		response = requests.get(url = url,cookies = cookie,headers = header)
	# print(dir(response))
	# print(response.encoding,response.headers['content-type'],response.apparent_encoding,requests.utils.get_encodings_from_content(response.text))
	response.encoding = 'gbk'
	HtmlCode = response.text
	return HtmlCode
def GetHtmlTree(url):
	HtmlCode = GetHtmlCode(url)
	HtmlTree = BeautifulSoup(HtmlCode,'html.parser')
	# print(HtmlTree)
	return HtmlTree
def GetKeyContent(url):
	HtmlTree = GetHtmlTree(url)
	# title = HtmlTree.h1.get_text()
	content = HtmlTree.find('div',id = 'content').get_text()
	error_code = {
	's3();':'','Se':'色','Y差Y错':'阴差阳错','nv':'女','未婚Q':'未婚妻','属X':'属性','无S':'无私','窃窃S语':'窃窃私语',
	'身T':'身体','T内':'体内','玄YT':'玄阴体','Y气':'阴气','cha在':'插在','裂T':'裂体','J天':'几天','爆T':'爆体','Y寒之气':'阴寒之气',
	'Y险':'阴险','P刻':'片刻',


	}
	for key,value in error_code.items():
		content = content.replace(key,value)
	return content

def JudgeChapter(chapterIndex):
	if os.path.exists(chapteIndexName):
		print('已存在章节：',chapteIndexName)
		return True

def SaveChapter(chapteIndexName,content):
	try:
		with open(chapteIndexName,'w') as f:
				f.write(content)
				f.close()
	except:
		os.system('del /s ' + chapteIndexName)

cursor.execute(cmd_list[0])
data = cursor.fetchall()
print(data)
print('章节总数:',len(data))
for index,line in enumerate(data):
	print('索引值:',index)
	chapteIndexName = str(index) + '.txt'
	isExist = JudgeChapter(chapteIndexName)
	if isExist:
		continue
		
	tmp_url = list(tuple(line))[-1]
	print(tmp_url)
	tmp_url_next =tmp_url[:-5] + '_2' +tmp_url[-5:]
	print(tmp_url_next)
	tmp_content = GetKeyContent(tmp_url)
	tmp_content_next = GetKeyContent(tmp_url_next)
	tmp_chapter = tmp_content + tmp_content_next
	SaveChapter(chapteIndexName,tmp_chapter.replace(u'\xa0', u' '))
	# break
	time.sleep(2)
	# break
# cmd = 'show tables;'
# cursor.execute(cmd)
 
# # 使用 fetchone() 方法获取单条数据.
# # data = cursor.fetchone()
# data = cursor.fetchall()

# print (data)
# cmd = 'select * from hunpo;'
# # cmd = 'insert into hunpo(title,url) values("nihao","hihi");'
# cursor.execute(cmd)
# db.commit()
# data = cursor.fetchone()
# cursor.execute('select * from hunpo;')
# data = cursor.fetchall()


# print (data)
# 关闭数据库连接
db.close()