#!/usr/bin/env python3
#coding=utf-8



class animo():
	def __init__(self,name,shengyin):
		self.name = name
		self.shengyin = shengyin
	def __str__(self):
		return ("{} is {} ".format(self.name,self.shengyin))
cat = animo('mao','wangwang')
print(cat)
