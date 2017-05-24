#!/usr/bin/envy python
'''
f = open('test.txt','r')
str = f.read()
print str
f.close()
with open('test.txt','r') as f:
	print f.read()
with open('test.txt','rb') as f:
	for line in f.readlines():
		print (line.strip())
with open('test.txt','wa+') as f:
	f.write('Hello,world!')
#print os.name
#print os.uname()
#print os.environ
#print os.getenv('PATH')
L = [x for x in os.listdir('.') if os.path.isdir(x)]
print L

'''

import os
print [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
