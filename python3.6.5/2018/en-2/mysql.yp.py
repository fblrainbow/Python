#!/usr/bin/env python3
#coding:utf-8
import pymysql
import re
import os
from bs4 import BeautifulSoup

# 打开数据库连接
db = pymysql.connect(host = 'localhost',user = 'root',passwd ='FBLATPX520@',db = 'fbl' )
 
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
 
# 使用 execute()  方法执行 SQL 查询 
# cursor.execute("SELECT VERSION()")
cmd_list = []

cmd_list.append('show tables;')

# cmd_list.append('insert into hunpo(title,url) values("adfsf","qml");')
# cmd_list.append('insert into hunpo(title,url) values("qml","fbl");')

cmd_list.append('select * from hunpo;')



tmp = []
for cmd in cmd_list:
	cursor.execute(cmd)
	data = cursor.fetchall()
	print(len(data))
	for line in data:
		tmp = list(tuple(line))
		print(tmp[-1])
# cmd = 'show tables;'
# cursor.execute(cmd)
 
# # 使用 fetchone() 方法获取单条数据.
# # data = cursor.fetchone()
# data = cursor.fetchall()

# print (data)
# cmd = 'select * from hunpo;'
# # cmd = 'insert into hunpo(title,url) values("nihao","hihi");'
# cursor.execute(cmd)
db.commit()
# data = cursor.fetchone()
# cursor.execute('select * from hunpo;')
# data = cursor.fetchall()




# print (data)
# 关闭数据库连接
db.close()




#可用