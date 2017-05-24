#!/usr/bin/env python
'''
#-*-coding:utf-8-*-
class Fib(object):
	def __init__(self):
		self.a,self.b = 0,1
	def __iter__(self):
		return self
	def next(self):
		self.a,self.b = self.b,self.a + self.b
		if self.a > 100000:		
		 	raise StopIteration()
		return self.a
for n in Fib():
	print n
class Fib(object):
	def __getitem__(self,n):
		a,b = 1,1
		for x in range(n):
			a,b = b,a+b
		return a
f = Fib()
def print_f(n):
 	for i in range(1,n):
		print f[i]
print_f(10)
class Fib(object):
	def __getitem__(self,n):
		if isinstance(n,int):
			a,b = 1,1
			for x in range(n):
				a,b = b,a+b
			return a
		if isinstance(n,slice):
			start = n.start
			stop = n.stop
			a,b = 1,1
			L = []
			for x in range(stop):
				if x >= start:
					L.append(a)
				a,b = b,a+b
			return L
f = Fib()
print f[0:5]
print f[:10]
print f[:10:2]
class Student(object):
	def __init__(self):
		self.name = 'Michael'
	def __getattr__(self,attr):
		if attr == 'ycore':
			return 99
s = Student()
print s.name,s.ycore
class Student(object):
	def __getattr__(self,attr):
		if attr == 'age':
			return lambda:25
s = Student()
print s.age()
class Student(object):
	def __getattr__(self,attr):
		if attr == 'age':
			return lambda:25
		raise AttributeError('\'Student\' object has no attribute\'%s\''%attr)
s = Student()
print s.agei()
class Chain(object):
	def __init__(self,path =''):
		self._path = path
	def __getattr__(self,path):
		return Chain('%s/%s'%(self.path,path))
	def __str__(self):
		return self._path
print Chain().status.user.timeline.list
'''
class Student(object):
	def __init__(self,name):
		self.name = name
	def __call__(self):
		print('My name is %s.'%self.name)
s = Student('Michael')
print s()
