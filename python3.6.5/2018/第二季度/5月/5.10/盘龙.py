#coding:utf-8
import requests
import re
from bs4 import BeautifulSoup

url = 'https://www.ybdu.com/xiaoshuo/2/2073/'

headers = {
	'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4882.400 QQBrowser/9.7.13059.400'
}

def getHtmlTree(url):
	r = requests.get(url,headers = headers)
	# print(r.status_code)
	# r.encoding = 'gbk'
	tmp = r.text
	htmlCode = BeautifulSoup(tmp,"html.parser")
	return htmlCode
def getUrl(url):
	HtmlTree = getHtmlTree(url)
	story = HtmlTree.find('meta',property="og:title")
	storyName = story['content']
	chapterList = HtmlTree.find('ul',"mulu_list")
	chapterList = chapterList.find_all('a')
	listChapter = []
	for element in chapterList:
		listChapter.append(url + '/' +element['href'])
	return (storyName,listChapter)
def getKey(url):
	HtmlTree = getHtmlTree(url)
	chapter = HtmlTree.h1.get_text()
	content = HtmlTree.find('div',id="htmlContent")
	content = content.get_text()
	flag = content.find('show')
	content = content[:flag]
	return (chapter,content)
if __name__ == '__main__':
	(storyName,chapterList) = getUrl(url)
	storyName = storyName + '.txt'
	for url in chapterList:
		tmp = []
		f = open(storyName,'a+',encoding='utf-8')
		(chapter,content) = getKey(url)
		tmp = chapter + '\n' + content
		print(chapter)
		f.write(tmp)
		f.close()

