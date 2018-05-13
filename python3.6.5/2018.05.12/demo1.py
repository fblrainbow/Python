#!/usr/bin/env python3
#coding:utf-8
# class Student(object):
# 	@property
# 	def birth(self):
# 		return self._birth

# 	@birth.setter
# 	def birth(self,value):
# 		self._birth=value
# 	@property
# 	def age(self):
# 		return 2018 - self._birth
# s = Student()
# s.birth(1992)


def getKeyWord(url):
	htmlTree = getHtmlTree(url)
	storyName = htmlTree.find('span',property="v:itemreviewed").get_text()
	storyInfo = htmlTree.find('div',id='info')
	storyInfoList = storyInfo.findAll('span')
	for line in storyInfoList:
		print(line)
		if -1 != line.get_text().find('作者'):
			storyAuthor = line.nextSibling
		else:
			storyAuthor = ''
		if -1 != line.get_text().find('出版社'):
			storyPublish = line.nextSibling.replace(' ','').replace('\n','')
		else:
			storyPublish = ''
		if -1 != line.get_text().find('出版年'):
			storyDate = line.nextSibling
		else:
			storyDate = ''
		if -1 != line.get_text().find('页数'):
			storyPages = line.nextSibling.replace(' ','').replace('\n','')
		else:
			storyPages = ''
		if -1 != line.get_text().find('定价'):
			storyPrices = line.nextSibling.replace(' ','').replace('\n','')
		else:
			stortPrices = ''
		if -1 != line.get_text().find('装帧'):
			storyGetUp = line.nextSibling.replace(' ','').replace('\n','')
		else:
			storyGetUp = ''
		if -1 != line.get_text().find('丛书'):
			storyTotleName = line.nextSibling.replace(' ','').replace('\n','')
		else:
			storyTotleName = ''
		if -1 != line.get_text().find('ISBN'):
			storyISBN = line.nextSibling.replace(' ','').replace('\n','')
		else:
			storyISBN = ''
	print('书名:%s'%storyName)
	print('作者:%s'%storyAuthor)
	print('出版社:%s'%storyPublish)
	print('出版年:%s'%storyDate)
	print('页数:%s'%storyPages)
	print('装帧:%s'%storyGetUp)
	print('丛书:%s'%storyTotleName)
	print('ISBN:%s'%storyISBN)
def isDefine(var):
	try:
		type(var)
	except:
		pass
try:
	type(afda)
except:
	print('adfad')
print(type(faf))