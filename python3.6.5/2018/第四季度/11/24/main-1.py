#!/usr/bin/env python
#coding:utf-8
import os
import sys
import path


def getFilePath(pathStr):
	dirList = [pathStr + '/' + str(line) + '.ts' for line in sorted([int(line[:-3]) for line in os.listdir(pathStr) if line.find('.ts') != -1])]
	
	return dirList
def readFile(fileName):
	with open(fileName,"r",encoding='utf-8') as f:
		bContent = f.read()
		return bContent
def saveFile(fileName,content):
    with open(fileName,"w") as f:
        f.write(content)
        f.close()

dirList = getFilePath('家庭瑜伽教师')
print(dirList)
str = "+".join(dirList)
print(str)
