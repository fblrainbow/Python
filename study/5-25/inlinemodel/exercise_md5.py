#!/usr/bin/env python
#-*-coding:utf-8-*-
import hashlib

md5 = hashlib.md5()
db = {'fbl':'20cf775fa6b5dfe621ade096f5d85d52','qml':1125}
for i in db:
	print '%s' %i,db[i]
