#!/usr/bin/env python
#-*-coding:utf-8-*-
'''
def now():
	print '2017-5-23'
f = now
print f()
print f.__name__
'''
'''
def log(func):
	def wrapper(*args,**kw):
		print'call %s():'%func.__name__
		return func(*args,**kw)
	return wrapper
@log
def now():
	print '2017-05-23'
print now.__name__,now()
'''
'''
import functools

def log(text):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args,**kw):
		 	print '%s %s():'%(text,func.__name__)
			return func(*args,**kw)
		return wrapper
	return decorator
@log('execute')
def now():
	print '2017-05-23'
print now()

print now.__name__
'''
def log(text):
	def decorator(func):
		def wrapper(*args,**kw):
			print '%s %s' %(text,func.__name__)
			return func(*args,**kw)
		return wrapper
	return decorator
@log('begin')
def call():
	pass
print call()



@log('end')
def call():
	pass
print call()

@log('')
def call():
	pass
print call()
