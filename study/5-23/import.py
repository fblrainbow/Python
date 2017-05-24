#!/usr/bin/env python
#-*-coding:utf-8-*-
try:
	import cStringIO as StringIO
except ImportError:
	import StringIO
def _private_1(name):
	return 'Hello,%s' %name
def _private_2(name):
	return 'Hi,%s' %name

def greeting(name):
	if len(name) > 3:
		return _private_1(name)
	else:
		return _private_2(name)
print greeting('asfd')
