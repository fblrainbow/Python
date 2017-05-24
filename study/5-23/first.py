#!/usr/bin/env python
#-*-coding:utf-8-*-
L = map(lambda x:x*x,range(1,10))
print L

def build(x,y):
	return lambda:x*x+y*y
print build(4,5)()
