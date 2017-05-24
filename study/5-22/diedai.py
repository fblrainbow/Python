#!/usr/bin/env python
#-*-coding:utf-8-*-
from collections import Iterable
print isinstance('abc',Iterable)
print isinstance([1,2,3],Iterable)
print isinstance(123,Iterable)
for i,value in enumerate(['A','B','C']):
	print i,value
for x,y in [(1,1),(2,4),(3,9)]:
	print x,y
