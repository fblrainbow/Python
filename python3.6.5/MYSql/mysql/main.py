#coding:utf-8

import requests
import json
import sys
sys.path.append(r'E:\Anaconda3\envs\python3.7\Lib\site-packages')
#print(sys.path)
import pymysql
import time
import os
#数据库数据处理
def readFile(fileName):
    with open(fileName,'r') as f:
        return f.read()

def mysql(host,user,passwd,db,content):
    
    db = pymysql.connect(host = host,user = user,passwd = passwd,db = db,charset='utf8' )
    #使用 cursor() 方法创建一个游标对象 cursor
    if type(content) == type('sf'):
        try:
            cursor = db.cursor()
            cursor.execute(content)
        
            print(cursor.fetchall())
        except:
            db.commit()
        
            db.close()
    else:
        print("list")
        try:
            cursor = db.cursor() 
            count = len(content)
            for index,line in enumerate(content):
                cursor.execute(line)
                if (index+1) % 10000 == 0:
                    print("完成进度{:.2f}%".format((index+1)*100/count))
        except:
            db.commit()
            db.close()

class DataBase(object):
    def __init__(self,host,user,passwd,db,cmdList):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.db = db
        self.cmdList = cmdList
    # 打开数据库连接
    def dbConnect(self):
        # db = pymysql.connect(host = 'localhost',user = 'root',passwd ='FBLATPX520@',db = 'pricedeep',charset='utf8' )
        dbConnect = pymysql.connect(host = self.host,user = self.user,passwd = self.passwd,db = self.db,charset='utf8' )
        self.dbConnect = dbConnect
        self.dbObject = self.dbConnect.cursor()
        self.t1 = time.time()
    #执行mysql命令
    def dbDeal(self):
        count = len(self.cmdList)
        for index,cmd in enumerate(self.cmdList):
            try:  #数据异常处理
                self.dbObject.execute(str(cmd))
                # print(self.dbObject.fetchall())
                if index % 10000 == 0:
                    print("进度{:.2f}%".format(index * 100 / count))
            except:
                self.cmdList.remove(cmd)
    #关闭数据库连接
    def dbClose(self):
        self.dbConnect.commit()
        self.dbConnect.close()
        self.t2 = time.time()
        print("插入总数据{}总计用时{:.3f}".format(len(self.cmdList),(self.t2-self.t1)))
    # 使用 cursor() 方法创建一个游标对象 cursor
    # cursor = db.cursor()
    # cursor.execute(content)
    # print(cursor.fetchall())
    # db.commit()
    # db.close()

class Data(object):  #数据序列类
    def __init__(self,dtName,fileList,rowSplit,colSplit,headName):
        self.fileList = fileList
        self.dtName = dtName
        self.rowSplit = rowSplit
        self.colSplit = colSplit
        self.headName = headName
    #获取数据记录
    def getDataRecord(self):
        flag = True
        #对每一个文件进行操作
        for line in self.fileList:
            #获取非空行记录
            dataRecordList = [x for x in readFile(line).replace('"','\'').split(self.rowSplit)[:] if x != '\n']
            #获取表格头字段
            colList = []
            #对每一条数据进行处理
            for x in dataRecordList[1:]:
                #获取每条记录的字段值
                colDataRecordList = [y for y in x.split(self.colSplit)]
                #一条sql数据值
                colList.append('(' + ','.join(colDataRecordList) + ')' )
            if flag:
                self.headNameList = dataRecordList[0].replace('\'','').split(self.colSplit)
                self.DataHeadNameUnit = ','.join(dataRecordList[0].replace('\'',"`").split(self.colSplit))
                self.colList = colList
                flag = False
            else:
                self.colList = self.colList + colList
    def getCmd(self):
        mysqlCmdList = ["INSERT INTO `IRSCFETS`(" + self.DataHeadNameUnit + ") " + "VALUES" + line + ";" for line in self.colList]
        self.cmdList = mysqlCmdList
        return (self.headNameList,self.cmdList)
#获取当前路径下的指定扩展名文件列表
def getExtendFileList(postfix):
    length = len(postfix)
    return [line for line in os.listdir() if line[-length:] == postfix]

if __name__ == "__main__":
    fileList = getExtendFileList('.csv') #获取当前文件夹下所有csv文件
    myData = Data('deepth',fileList,'\n',',',True) #获取数据记录
    myData.getDataRecord()
    (headNameList,cmdList) = myData.getCmd()   #数据翻译成sql
    mysql('localhost','root','FBLATPX520@','cfets',"drop table irscfets;")
    creatTableSql = 'CREATE TABLE IRSCFETS(' + ' varchar(255),'.join(headNameList) + ' varchar(255)' + ');' 
    print(creatTableSql,len(cmdList))
    print(cmdList[0])
    mysql('localhost','root','FBLATPX520@','cfets',creatTableSql)
    
    mysql('localhost','root','FBLATPX520@','cfets',cmdList)
    '''
    creatTableSql = 'CREATE TABLE IRSCFETS(' + ' varchar(255),'.join(headNameList) + ' varchar(255)' + ');' 
    fbl = []
    print(creatTableSql)
    fbl.append(creatTableSql)
    demo1 = DataBase('localhost','root','FBLATPX520@','cfets',fbl)#创建类
    
    demo1.dbConnect()#连接数据库
    demo1.dbDeal()#数据处理
    demo1.dbClose()#commit 并关闭数据库连接
    print("成功创建表")

    length = len(cmdList)    #原始数据量
    myDataDeal = DataBase('localhost','root','FBLATPX520@','cfets',cmdList)#创建类
    myDataDeal.dbConnect()#连接数据库
    myDataDeal.dbDeal()#数据处理
    myDataDeal.dbClose()#commit 并关闭数据库连接
    '''

