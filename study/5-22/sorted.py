#!/usr/bin/env python
#-*-coding:utf-8-*-
L = [554,456,456,87,452,103,454]
print sorted(L)

def reversed_cmp(x,y):
	if x > y:
		return -1
	if x < y:
		return 1
	return 0

print sorted(L,reversed_cmp)
