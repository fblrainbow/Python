#coding:utf-8
import re
import os
import requests
import sys

from bs4 import BeautifulSoup
import urllib


cookies = {
    'Cookie':'uuid_tt_dd=10_30709694610-1527791691256-470312; UserName=qq_37608398; UserInfo=YleRigef8jqAcRgUEr8XfvnHyGiTFj91IMxMdgCPhEzSSyUbrddA4mExsrlGQYhg5bZ3AaqyG1QoxLTiGd1kTsZSxyk7VQOSiobYpZKfFY4%3D; UserNick=RainbowJhon; UN=qq_37608398; AU=2FB; BT=1527852570586; Hm_ct_6bcd52f51e9b3dce32bec4a3997715ac=1788*1*PC_VC; smidV2=20180601192836bf3e650eaaa41b4e25a7181e3aa97a1000ce4894db65a9a20; dc_tos=p9n8eg; dc_session_id=10_1527791691256.526264; Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac=1527791688,1527853147,1527853186; Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac=1527854920'
    }

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.5155.400 QQBrowser/9.7.13231.400'
}

urlWeb = 'http://www.xinshubao.net/0/927/'

def getHtmlCode(url):
    pageWebMain = requests.get(url,cookies = cookies,headers = headers)
    pageWebMain.encoding = 'utf-8'
    pageWebMainCodeHtml = pageWebMain.text
    htmlCode = BeautifulSoup(pageWebMainCodeHtml,'html.parser')
    return htmlCode
class story:
    def __init__(self,url):
        self.url = url
    def getStoryName(self):
        htmlCode = getHtmlCode(self.url)
        storyName = htmlCode.h1.get_text()
        print(storyName)
        return storyName
    def getChapterUrlList(self):
        chapterListKeyContent = {}
        htmlCode = getHtmlCode(self.url)
        chapterList = htmlCode.find('ul',class_='_chapter')
        chapterListA = chapterList.find_all('a')
        for line in chapterListA:
            chapterTotleName = line.get_text()
            chapterNameDeal = chapterTotleName.split(' ')
            chapterNameHeadTmp = chapterNameDeal[0]
            chapterNameHead = chapterNameHeadTmp.replace('1','一').replace('2','二').replace('3','三').replace('4','四').replace('5','五').replace('6','六').replace('7','七').replace('8','八').replace('9','九').replace('10','十')
            chapterNameEnd = chapterNameDeal[-1]
            chapterUrl = line['href'].replace('\r\n','')
            chapterListKeyContent[chapterNameHead] = {chapterNameEnd:chapterUrl}
        return chapterListKeyContent
    def getChapterContent(self,urlHead):
        htmlCode = getHtmlCode(urlHead)
        storyContent = htmlCode.find('div',id='content')
        storyContent = storyContent.get_text().replace('\r\n','')
        return storyContent
    def saveChapterContent(self,storyName,storyContent):
        f = open(storyName,'a',encoding = 'utf-8')
        f.write(storyContent)
        f.close()
if __name__ == '__main__':
    hunpo = story(urlWeb)
    chapterListKeyContent = hunpo.getChapterUrlList()
    storyName = hunpo.getStoryName() + '.txt'
    cmd = 'del /s ' + storyName
    os.system(cmd)
    for chapterNumber,chapterDict in chapterListKeyContent.items():
        for chapterName,chapterUrl in chapterDict.items():
            print(chapterNumber)   
            contentTmp1 = hunpo.getChapterContent(chapterUrl)
            chapterUrl_2 = chapterUrl[:-5] + '_2' + chapterUrl[-5:]
            contentTmp2 = hunpo.getChapterContent(chapterUrl_2)
            contentChapter = contentTmp1 + contentTmp2 + '\r\n'
            hunpo.saveChapterContent(storyName,contentChapter)