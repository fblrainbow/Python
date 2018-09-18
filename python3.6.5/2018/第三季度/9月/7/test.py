#!/usr/bin/env python
#coding=utf-8
#__author__ = 'Administrator'
l = range(8)
mylist = ['q','w','e','r','a','s','d','f']
mylist = l
d = {}
for x in mylist:
     d[x] = 1
mylist = list(d.keys())
print(mylist)