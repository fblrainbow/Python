#!/usr/bin/env python
#-*-coding:utf-8-*-
try:
	import cPickle as pickle
except ImportError:
	import pickle
'''
d = dict(name = 'Bob',age = 20,score = 88)
f = open('dump.txt','wb')
pickle.dump(d,f)
f.close()
'''
f = open('dump.txt','rb')
d = pickle.load(f)
f.close()
print d
