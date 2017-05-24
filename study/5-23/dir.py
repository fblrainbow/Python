#!/usr/bin/env python
#-*-coding:utf-8-*-
'''
print dir('ABC')
print len('ABC')
print 'ABC'.__len__()
class MyObject(object):
	def __len__(self):
		return 100
obj = MyObject()
print len(obj)
print 'abc'.upper()
'''
class MyObject(object):
	def __init__(self):
		self.x = 9
	def power(self):
		return self.x * self.x
obj = MyObject()
print hasattr(obj,'x')
print obj.x
setattr(obj,'y',19)
print hasattr(obj,'y')
print getattr(obj,'y')
print obj.y
print getattr(obj,'z',404)
