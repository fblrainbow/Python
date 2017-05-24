#!/usr/bin/env python
#-*-coding:utf-8-*-
def f(x):
	return x*x
L = map(f,range(1,11))
print L
S = map(str,range(1,10))
print S
		
def add(x,y):
	return x+y
print reduce(add,[1,3,5,7,9])

def transform(x,y):
	return 10*x+y
print reduce(transform,[1,3,5,7,9])
def char2num(s):
	return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]

def str2int(s):
	def fn(x,y):
		return x*10+y
	def char2num(s):
		return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
	print reduce(fn,map(char2num,s))
