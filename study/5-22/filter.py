#!/usr/bin/env python
#-*-coding:utf-8-*-
def is_odd(n):
	return n%2 == 1
L = filter(is_odd,[1,2,4,5,6,9,10,15])
print L
def not_empty(s):
	return s and s.strip()
S = filter(not_empty,['A','','B',None,'C','  '])
print S
