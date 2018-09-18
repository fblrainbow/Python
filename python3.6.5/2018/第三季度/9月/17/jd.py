#!/usr/bin/env python
#coding=utf-8
#__author__ = 'Administrator'
import pymysql.cursors

connection = pymysql.connect(
                             host = 'localhost',      #数据库地址，本地一般写127.0.0.1或者localhost
                             user = 'root',            #数据库账户
                             password = 'FBLATPX520@',#数据库密码
                             db = 'mysql',             #使用的数据库名称
                             charset = 'utf8mb4',      #字符集
                             #cursorclass=pymysql.cursors.DictCursor
                             )
try:
    with connection.cursor() as cursor:
        # Create a new record
        sql = "Create database qinmeilin;"
        cursor.execute(sql)

        connection.commit()               #如果是写操作需要提交才能生效
        result = cursor.fetchall()    #获取上一次的执行结果
        print(type(result))
        print(result)
finally:
    connection.close()        #关闭数据库