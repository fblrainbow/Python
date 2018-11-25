#!/usr/bin/env python
#coding:utf-8
import os
import sys
def getFatherName():
	fatherName = os.path.abspath(__file__).split('\\')[-2:-1][0]
	return fatherName
def getFilePath():
	dirList = [str(line) + '.ts' for line in sorted([int(line[:-3]) for line in os.listdir() if line.find('.ts') != -1])]
	return dirList
def readFile(fileName):
	with open(fileName,"r",encoding='utf-8') as f:
		bContent = f.read()
		return bContent
def saveFile(fileName,content):
    with open(fileName,"w") as f:
        f.write(content)
        f.close()

dirList = getFilePath()
string = "+".join(dirList)
print(string)
stringTmp = "del " + getFatherName() + ".mp4"
os.system(stringTmp)
string = "copy /b " + string + " = " + getFatherName() + ".mp4"
os.system(string)
