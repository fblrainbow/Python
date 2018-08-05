#!/usr/bin/env python3
#coding:utf-8
import pymysql

# 打开数据库连接
db = pymysql.connect(host = 'localhost',user = 'root',port=3306,passwd ='FBLAPTX520@',db = 'fanbinglin' )

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询 
# cursor.execute("SELECT VERSION()")
cmd_list = []
cmd_list.append('show tables;')
cmd_list.append('insert into hunpo(title,url) values("adfsf","qml");')
cmd_list.append('insert into hunpo(title,url) values("qml","fbl");')

cmd_list.append('select * from hunpo;')
for cmd in cmd_list:
    cursor.execute(cmd)
    data = cursor.fetchone()
    print(data)
#提交数据
db.commit()
# 关闭数据库连接
db.close()
print('dfs')