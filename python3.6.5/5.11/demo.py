
#coding:utf-8
import requests
import re
import urllib
from bs4 import BeautifulSoup

url = 'http://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gbk&word=64k%B3%AC%B8%DF%C7%E5%B7%D6%B1%E6%C2%CA%CD%BC%C6%AC&fr=ala&ala=1&alatpl=adress&pos=0&hs=2&xthttps=000000'

headers = {
	'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4882.400 QQBrowser/9.7.13059.400'
}
def getCode(url):
	r = urllib.open(url)
	# print(r.status_code)
	# print(r.)
	tmp = r.read()
	return tmp
def getHtmlTree(url):
	r = requests.get(url,headers = headers)
	# print(r.status_code)
	# print(r.)
	r.encoding = 'UTF-8'
	tmp = r.text
	htmlTree = BeautifulSoup(tmp,"html.parser")
	return htmlTree
# print(getHtmlTree(url))
def getUrlList(url):
	HtmlTree = getHtmlTree(url)
	imgList = HtmlTree.find_all('img')
	# print(imgList)
	UrlList = []
	for imgUrl in imgList:
		if imgUrl.get('src') :
			UrlList.append('http:' + imgUrl.get('src'))
	return UrlList
if __name__ == '__main__':
	UrlList = getUrlList(url)
	for key,url in enumerate(UrlList):
		imgName = str(key) + '.jpg'
		f = open(imgName,'w+',encoding = 'utf-8')
		tmp = getCode(url)
		f.write(tmp)
		f.close()
