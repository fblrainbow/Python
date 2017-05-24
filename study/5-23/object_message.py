#!/usr/bin/env python
#-*-coding:utf-8-*-
'''
print type(213)
print type('str')
print type(None)
print type(abs)
f=abs
print type(abs)==type(f)
print type('13')==type(13)
'''
import types
print type('abc')==types.StringType
print type(u'abc')==types.UnicodeType
print type([])==types.ListType
print type(str)==types.TypeType
