#!/usr/bin/env python
#-*-coding:utf-8-*-
def calc_sum(*args):
	ax = 0
	for n in args:
		ax += n
	return ax
def lazy_sum(*args):
	def sum():
		ax = 0
		for n in args:
			ax += n
		return ax
	return sum
f = lazy_sum(1,3,5,7,9)
print f()

def count():
	fs = []
	for i in range(1,4):
		def f(i):
			def g():
				return i*i
			return g
		fs.append(f(i))
	return fs
f1,f2,f3 = count()
print f1(),f2(),f3()





