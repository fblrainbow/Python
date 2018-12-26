#coding:utf-8

import requests
from lxml import etree

def getContent(url):
	response = requests.get(url = url)
	response = etree.HTML(response.content)
	content = '\n'.join(response.xpath('//*[@id="content"]/text()'))
	title = response.xpath('/html/body/div[2]/div[2]/div[1]/h1/text()')[0]
	print(url,title)
	return title + "\n" + content + "\n"
	
def saveFile(filename,content):
    try:
        with open(filename,"a+",encoding='utf-8') as f:
            f.write(content)
            f.close()
    except:
        pass

class Story(object):
	def __init__(self,url):
		self.url = url
	def getCode(self):
		response = requests.get(url = self.url)
		self.content = response.content
		# print(response.text)
	def getHtmlStruct(self):
		self.struct = etree.HTML(self.content)
		self.storyName = self.struct.xpath('/html/body/div[3]/div[1]/div[2]/h1/text()')
		return self.storyName
	def getChapterList(self):
		chapterList = [self.url + str(x) + '.html' for x in sorted([int(line[:-5]) for line in self.struct.xpath('/html/body/div[3]/div[2]/ul/li/a/@href')])]
		# print(chapterList)
		return chapterList


if __name__ == "__main__":
	url = "https://www.i7wx.com/book/41/41628/"
	story = Story(url)
	story.getCode()
	storyName = story.getHtmlStruct()[0]
	chapterList = story.getChapterList()
	for line in chapterList[2028:]:#2000章开始
		string = getContent(line)
		saveFile(storyName + ".txt",string)
		 