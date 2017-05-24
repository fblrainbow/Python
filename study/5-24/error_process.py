#!/usr/bin/env python
#-*-coding:utf-8-*-
'''
try:
	print 'try...'
	r = 10 / 1
	print 'result:',r
except ZeroDivisionError,e:
	print 'except:',e
finally:
	print 'finally...'
print 'END'
try:
	print 'try...'
	r = 10 / 0
	print 'result:',r
except ValueError,e:
	print 'ValueError:',e
except ZeroDivisionError,e:
	print 'ZeroDivisionError:',e
else:
	print 'no error!'
finally:
	print 'finally...'
print 'END'
import logging
def foo(s):
	return 10 / int(s)
def bar(s):
	return foo(s)*2
def main():
	try:
		bar('0')
	except StandardError,e:
		logging.exception(e)
print main()
print 'END'
class FooError(StandardError):
	pass
def foo(s):
	n = int(s)
	if n == 0:
		raise FooError('invalid value:%s' %s)
	return 10/n

'''
def foo(s):
	n = int(s)
	return 10/n
def bar(s):
	try:
		return foo(s)*2
	except StandardError,e:
		print 'Error!'
		raise
def main():
	bar('0')
main()
