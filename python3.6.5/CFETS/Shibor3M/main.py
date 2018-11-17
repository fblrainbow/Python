#coding:utf-8

import requests
import json
import pymysql
import os
import sys
import time

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


    # 使用 execute()  方法执行 SQL 查询
    # cursor.execute("SELECT VERSION()")
    # cmd_list = []
    #
    # cmd_list.append('show tables;')
    # cmd_list.append('select * from IssueCode;')
# cmd_list.append('select * from stock;')
# cmd_list.append('insert into hunpo(title,url) values("adfsf","qml");')
# cmd_list.append('insert into hunpo(title,url) values("qml","fbl");')

#
# for cmd in cmd_list:
#     cursor.execute(cmd)
#     data = cursor.fetchone()
#     print(data)
#提交数据
# db.commit()
# 关闭数据库连接
# db.close()

class Shibor3M(object):
    def __init__(self,url,headers,cookies):
        self.url = url
        self.headers = headers
        self.cookies = cookies
    def getJson(self):
        sourcejson = requests.post(url = self.url,headers = self.headers,cookies = self.cookies)
        if sourcejson.status_code != 200:
            return
        sourcejson = sourcejson.content
        # sourcejson = sourcejson.decode("utf-8")
        jsonSource = json.loads(sourcejson)
        for k,v in jsonSource.items():
            # print(k,type(v),v)
            pass
        jsonDict = {}
        jsonDict["curveType"] = jsonSource["data"]["curveType"]
        jsonDict["curveTypeEn"] = jsonSource["data"]["curveTypeEn"]
        jsonDict["cfgItemType"] = jsonSource["data"]["cfgItemType"] #curveId
        jsonDict["curveId"] = jsonSource["data"]["curveId"] #curveId
        try:
            jsonDict["options"] = jsonSource["data"]["options"] [jsonDict["curveId"]] or ""#curveId
        except:
            jsonDict["options"] = ""
        jsonDict["quoteTime"] = jsonSource["data"]["quoteTime"]
        jsonDict["showDateCN"] = jsonSource["data"]["showDateCN"]
        jsonDict["showDateEN"] = jsonSource["data"]["showDateEN"]
        jsonDict["provider"] = jsonSource["head"]["provider"]
        jsonDict["ts"] = jsonSource["head"]["ts"]
        jsonDict["tstext"] = jsonSource["head"]["tstext"]
        try:
            jsonDict["records"] = jsonSource["records"]
        except:
            jsonDict["records"] = ""
        jsonDict["issueCode"] = {}
        if jsonDict["records"] != "":
            for index,line in enumerate(jsonDict["records"]):
                jsonDict["issueCode"][jsonDict["curveTypeEn"] + "_" + line["tl"]] = [line["tl"],line["optimalAvg"],line["optimalAsk"],line["optimalBid"],line["curveid"]]
        for k,v in jsonDict["issueCode"].items():
            # print(k,jsonDict["showDateCN"],jsonDict["quoteTime"],jsonDict["curveTypeEn"],jsonDict["cfgItemType"],jsonDict["curveId"],jsonDict["options"],jsonDict["provider"],jsonDict["tstext"],v,)
            str = "insert into IRS_CFETS(IssueCode,showDateCN,quoteTime,curveTypeEn,cfgItemType,curveId,options,provider,tstext,tl,optimalAvg,optimalAsk,optimalBid) value('{IssueCode}','{showDateCN}','{quoteTime}','{curveTypeEn}','{cfgItemType}','{curveId}','{options}','{provider}','{tstext}','{tl}','{optimalAvg}','{optimalAsk}','{optimalBid}');"\
                .format(IssueCode = k,showDateCN = jsonDict["showDateCN"],quoteTime = jsonDict["quoteTime"],curveTypeEn = jsonDict["curveTypeEn"],cfgItemType = jsonDict["cfgItemType"],curveId = jsonDict["curveId"],options = jsonDict["options"],provider = jsonDict["provider"],tstext = jsonDict["tstext"],tl = v[0] ,optimalAvg = v[1],optimalAsk = v[2],optimalBid = v[3])
            print(str)
            dataDeal(str)


        # for line in jsonSource["records"]:
        #     Timer = line["tl"]
        #     jsonDict[Timer] =
def saveFile(filename,content):
    with open(filename,"a+") as f:
        f.writelines(content)
        f.close()
def readFile(filename):
    with open(filename,"r") as f:
        content = f.read()
        print(content)
        return content


if __name__ == "__main__":

    url = "http://www.chinamoney.com.cn/chinese/bkcurvfx/"   #总网站
    url = "http://www.chinamoney.com.cn/ags/ms/cm-u-bk-shibor/Ifcc?lang=CN&curveId=15&cfgItemType=71"
    for i in range(71,82,1):
        for k in [15,16,17]:
            print(i,k)
            url = "http://www.chinamoney.com.cn/ags/ms/cm-u-bk-shibor/Ifcc?lang=CN&curveId=" + str(k) + "&cfgItemType=" + str(i)
            cookies = {"_ulta_id.CM-Prod.e9dc":"a9368f3ef87b02ca"}
            headers = {"Accept":"application/json,text/javascript,*/*;q=0.01","Accept-Encoding":"gzip,deflate","Accept-Language":"zh-CN,zh;q=0.9","User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}
            shibor3M = Shibor3M(url,headers,cookies)
            jsonRet = shibor3M.getJson()
    strTime = time.ctime() + '\n'
    saveFile("cfets.txt",strTime)
    readFile("cfets.txt")