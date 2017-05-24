#!/usr/bin/env python
#-*-coding:utf-8-*-
#面向过程

std1 = {'name':'Michael','score':98}
std2 = {'name':'Bob','score':81}
def print_score(std):
	print '%s:%s'%(std['name'],std['score'])
print print_score(std1),print_score(std2)

#面向对象
class Student(object):
	def __init__(self,name,score):
		self.name = name
		self.score = score

	def print_score(self):
		print '%s:%s' %(self.name,self.score)
bart = Student('Bart Simpson',59)
lisa = Student('Lisa Simpson',87)
print bart.print_score()
print lisa.print_score()





