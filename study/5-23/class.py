#!/usr/bin/env python 
#-*-coding:utf-8-*-
'''
class Student(object):
	pass
bart = Student()
bart.name = 'Bart Simpson'
print bart.name
class Student(object):
	def __init__(self,name,score):
		self.name = name
		self.score = score
	def print_score(self):
		print '%s:%s' %(self.name,self.score)
bart = Student('Bart Simpson',59)
print bart.print_score()
'''
class Student(object):
	def __init__(self,name,score):
		self.name = name
		self.score = score	
	def get_grade(self):
		if self.score >= 90:		
			return 'A'
		elif self.score >= 60:
			return 'B'
		else:
			return 'C'
bart = Student('Bart Simpson',59)
print bart.get_grade()










