#!/usr/bin/env python 
#-*-coding:utf-8-*-
import re

'''
test='rwrwrwrpython313'
def exe():
	if re.match(r'py',test):
		print 'OK'
	else:
		print 'Failure'
exe()
m = re.match(r'^(\d{3})-(\d{5,12})$','012-13212181728')
print m.group(0)

'''
re_mail = re.compile(r'^(\d+@\w+).(\w+)$')
mail1 = '846058904@qq.com'
print re_mail.match(mail1).groups()
