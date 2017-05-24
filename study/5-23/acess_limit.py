#!/usr/bin/env python
#-*-coding:utf-8-*-
class Student(object):
	def __init__(self,name,score):
		self.__name = name
		self.__score = score
	def print_score(self):
		print '%s:%s'%(self.__name,self.__score)
	def get_name(self):
		return self.__name
	def get_score(self):
		return self.__score
bart = Student('Bart Simpson',98)
print bart.print_score()
print bart.get_score()
bart._Student__name = 'bart'
print bart.print_score()
