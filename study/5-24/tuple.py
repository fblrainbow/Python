#!/usr/bin/env python
#-*-coding:utf-8-*-
'''
from hello import Hello
h = Hello()
print h.hello()
print (type(h))
'''
def fn(self,name = 'world'):
	print ('Hello,%s.'%name)
Hello = type('Hello',(object,),dict(hello=fn))
h = Hello()
print h.hello()
print (type(Hello))
print (type(h))
