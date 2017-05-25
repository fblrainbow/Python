#!/usr/bin/env python 
#-*-coding:utf-8-*-
import hashlib
md5 = hashlib.md5()
md5.update('846058904')
#md5.update('python hashlib?')
print md5.hexdigest()
md5.update('1065797005')
#md5.update('python hashlib?')
print md5.hexdigest()
