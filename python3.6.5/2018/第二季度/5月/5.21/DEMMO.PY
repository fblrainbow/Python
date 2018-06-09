
#!/usr/bin/env python3
#coding:utf-8

import re
import os
import sys
import requests
from bs4 import BeautifulSoup

cookies = {
		'Cookie':'NTESSTUDYSI=163d9e7a8b0342b9bf0e2f9df11a83bf; EDUWEBDEVICE=4ddd60430ba24d3cae8da0cc90de34af; utm=eyJjIjoiIiwiY3QiOiIiLCJpIjoiIiwibSI6IiIsInMiOiIiLCJ0IjoiIn0=|aHR0cHM6Ly93d3cuYmFpZHUuY29tL2xpbms/dXJsPWRZcEoxcnVzVTRyalVJbXlGRWlIeGR3SEhPZ1E0MFVCaGlJbG5VRXljTU8md2Q9JmVxaWQ9OWVlYTc3YWUwMDAwY2U2NjAwMDAwMDA2NWFmOTllZDA=; __f_=1526308565315; _ntes_nnid=64e66c4f7fa805ff7c2f62bb28215a2b,1526308546872; _ntes_nuid=64e66c4f7fa805ff7c2f62bb28215a2b; STUDY_INFO=A4CBF69253E936633819A2E772C5B807|4|1017253490|1526308591080; STUDY_SESS="cdQiMkHxjgM2g1a8+nGLxvW/S9rHBvqWQ9d2/F/Iswd1SsMmOtwZq0ZLr8is17d3qHiHb3csHPbhGWIzezlInokLXq+FiD/fDa0zp6fkzsU6WCZ2Oggpp2O5LfS8kRQ5YxFHjfsseVsiMapRgbdjS/x5pJnN6BQekm4gPcN3+WrdNz5i9lFcIuPSeV3m+gdggAd9uMV3AXu6jiU0a69PwA=="; STUDY_PERSIST="DhADfXy6Rdc49pG3ugDYdA0eQ/sddhDSDyj//I+0nfCcwAJosApYZSQh51LLCP4ULGLGANnMZdxhuHMwA6VZaWzNXg5fDP1piBNj/8/cui8z+oM1FaHBxarpbNZak5qTzysDjxic8TPMFqyQzyvHUdUSSTbbZkN0a139NYJxVWhoAz5rxcfapAwDdUXQMZONI0f2VTFzD+aF4EVJIV6IcTO448lOV8V7ewmTqLW5HHBm1qaJZ4DNwobZ7X76taGMo715LQWdFWnunKzE3cO8yZb7By9sL3t1+Lz3aQPZ79s="; NETEASE_WDA_UID=1017253490#|#1463721041349; NTES_STUDY_YUNXIN_ACCID=s-1017253490; NTES_STUDY_YUNXIN_TOKEN=e8ee331e5dab7f16718126323d206d74; __utma=129633230.170383641.1526308545.1526308545.1526308545.1; __utmb=129633230.15.9.1526308592055; __utmc=129633230; __utmz=129633230.1526308545.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic'

}

headers = {
		'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4882.400 QQBrowser/9.7.13059.400'
}
url = 'http://www.7mav4.com/5644/%E6%AC%A7%E7%BE%8E%E6%BD%AE%E5%90%B9%E5%90%88%E9%9B%86%E4%B9%8B%E8%A2%AB%E9%BB%91%E5%A4%A7%E5%B1%8C%E6%93%8D%E5%88%B0%E5%96%B7%E6%B0%B4%E7%AF%87/'
url = 'http://www.7mav4.com/8190/%E5%88%9A%E5%8F%91%E8%82%B2%E5%A5%BD%E7%9A%84%E5%B0%8F%E5%A6%B9%E5%A6%B9%E5%AE%B6%E4%B8%AD%E8%87%AA%E6%8B%8D%E9%A6%99%E8%95%89%E8%87%AA%E6%85%B0%E6%BD%AE%E5%90%B9%E5%96%B7%E6%B0%B4/'
url = 'http://www.nyf4.com/7.htm'
url = 'http://www.nyf4.com/AAbook/AAAtb/xiaoyuan/index-3.html'  #一页
url = 'http://www.nbg4.com/AAtupian/AAAtb/asia/index-2.html'  #一章
urlHead = 'http://www.nyf4.com'
url = 'http://www.nyf4.com/AAtupian/AAAwz/128931.html'

def getHtmlTree(url):
	# time.sleep(3)
	tmp = requests.get(url,cookies = cookies,headers = headers)
	tmp = requests.get(url,headers = headers)
	if 200 != tmp.status_code:
		print('请求异常，返回码为%s'%tmp.status_code)
		exit()
	tmp.encoding='utf-8'
	text = tmp.text
	htmlTree = BeautifulSoup(text,'html.parser')
	return htmlTree
def getBody(url):
	tmp = requests.get(url,cookies = cookies,headers = headers)
	tmp = requests.get(url,headers = headers)
	if 200 != tmp.status_code:
		print('请求异常，返回码为%s'%tmp.status_code)
		exit()
	tmp.encoding='utf-8'
	body = tmp.content
	return body
def getImgList(url):
	htmlTree = getHtmlTree(url)
	title = htmlTree.h1.get_text()
	img = htmlTree.find_all('img')
	imgUrlList = []
	for imgUrl in img:
		imgUrlList.append(imgUrl['src'])
	return (title,imgUrlList)
url = 'http://www.nbg4.com/AAtupian/AAAwz/129045.html'
# print(getImgList(url))
def getPageList(url):
	htmlTree = getHtmlTree(url)
	textList = htmlTree.find_all('ul')
	liList = textList[-1]
	li = liList.find_all('a')
	urlList=[]
	for line in li:
		line = line['href']
		line = urlHead + line
		urlList.append(line)
	# print(urlList)
	return urlList
def isDefine(var):
	try:
		type(var)
	except NameError:
		print('变量%s未定义'%var)
	except:
		pass
def saveImg(title,imgUrlList):
	count = len(imgUrlList)
	cmd = 'del /q *.jpg'
	os.system(cmd)
	try:
		for i in range(0,count):
			if not os.path.exists(title):
				cmd = 'mkdir ' + title
				os.system(cmd)
			body = getBody(imgUrlList[i])
			f = open(str(i) + '.jpg','wb+')
			f.write(body)
			f.close()
		cmd = 'move /y *.jpg ' + title
		os.system(cmd)
	except:
		pass
# page url = 'http://www.nyf4.com/AAbook/AAAtb/xiaoyuan/index-3.html'

pageUrl = 'http://www.nbg4.com/AAtupian/AAAtb/asia/index'
# pageUrl = 'http://www.nbg4.com/AAtupian/AAAtb/oumei/index'
if __name__ == '__main__':
	for index in range(33,200):
		pageUrlTmp = pageUrl + '-' + str(index) +'.html'
		print('Page = %s'%pageUrlTmp)
		urlList = getPageList(pageUrlTmp)
		try:
			for line in urlList:
				(title,imgUrlList) = getImgList(line)
				print('line = %s---%s'%(index,line))
				saveImg(title,imgUrlList)
		except:
			pass
	(title,imgUrlList) = getImgList(url)
	print(title,imgUrlList)
	saveImg(title,imgUrlList)
