#!/usr/bin/env python
#coding=utf-8
#__author__ = 'Administrator'
from lxml import etree
import requests

class Stock():
    def __init__(self,url):
        self.url = url
    def GetHtmlStruct(self):
        response = requests.get(self.url)
        response.encoding = 'gbk'
        response = response.content
        response = str(response,encoding = "gbk")
        htmlStruct = etree.HTML(response)
        self.htmlStruct = htmlStruct
    def GetKeyInfo(self):
        hrefList = self.htmlStruct.xpath('/html/body/div[9]/div/ul/li/a/@href')
        nameList = self.htmlStruct.xpath('/html/body/div[9]/div/ul/li/a/text()')

        stockID = []
        stockName = []
        for line in nameList:
            flag1 = line.find('(')
            flag2 = line.find(')')
            stockID.append(line[flag1+1:flag2])
            stockName.append(line[flag2+1:])
        combine = dict(zip(stockID,stockName))
        self.combine = combine
    def Save(self):
        with open("stock.txt","w+") as f:
            f.write(str(self.combine))
            f.close()




if __name__ == "__main__":
    url = 'http://quote.eastmoney.com/hk/HStock_list.html'
    s = Stock(url)
    s.GetHtmlStruct()
    s.GetKeyInfo()
    s.Save()
