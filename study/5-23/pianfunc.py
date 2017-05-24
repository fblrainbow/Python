#!/usr/bin/env python
#-*-coding:utf-8-*-
'''
print int('12345')
print int('1334',base=8)
print int('1334',base=16)
print int('1334',base=12)
'''
'''
def int2(x,base=2):
	return int(x,base)
print int2('10100101000'),int2('1000010')
'''
import functools
int2 = functools.partial(int,base=2)
print int2('1001')
