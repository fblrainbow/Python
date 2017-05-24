#!/usr/bin/env python
#-*-coding:utf-8-*-
'''
class Student(object):
	pass
s = Student()
s.name = 'Michael'
print s.name
def set_age(self,age):
	self.age = age
from types import MethodType
s.set_age = MethodType(set_age,s,Student)
s.set_age(25)
print s.age
s2 = Student()
s2.set_age(25)
print s2.age
def set_score(self,score):
	self.score = score
Student.set_score = MethodType(set_score,None,Student)
s.set_score(100)
print s.score
s2 = Student()
s2.set_score(65)
print s2.score
class Student(object):
	__slots__ = ('name','age')
s = Student()
s.name = 'Michael'
s.age = 29	 
print s.name,s.age
class GraduateStudent(Student):
	pass
g = GraduateStudent()
g.score = 3445
print g.score






class Student(object):
	def get_score(self):
		return self.score
	def set_score(self,value):
		if not isinstance(value,int):
			raise ValueError('score must be integer!')
		if value < 0 or value > 100:
			raise ValueError('score must between 0~100!')
		self.score = value
s = Student()
s.set_score(60)
print s.get_score()
s.set_score(34)
print s.get_score()

class Student(object):
	@property
	def score(self):
		return self._score
	
	@score.setter
	def score(self,value):
		if not isinstance(value,int):
			raise ValueError('score must be an integer!')
		if value < 0 or value > 100:
			raise ValueError('score must between 0~100!')
		self._score = value
s = Student()
s.score = 80
print s.score
s2 = Student()
s2.score = 100
print s2.score
'''



class Student(object):
	@property
	def birth(self):
		return self._birth
	
	@birth.setter
	def birth(self,value):
		self._birth = value
	@property
	def age(self):
		return 2014 - self._birth
s = Student()
s.birth = 45
print s.age
