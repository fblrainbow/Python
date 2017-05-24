#!/usr/bin/env python
#-*-coding:utf-8-*-
print range(1,11,2)
L = []
for x in range(1,11):
	L.append(x*x)
print L
	
print [x*x for x in range(1,11)]
