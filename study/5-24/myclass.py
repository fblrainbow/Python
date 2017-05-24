#!/usr/bin/env python
#-*-coding:utf-8-*-
class Student(object):
	def __init__(self,name):
		self.name = name
	def __str__(self):
		return 'Student object (name: %s)'%self.name
print Student('Michael')
print dir(Student)
