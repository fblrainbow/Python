#!/usr/bin/env python3
#encoding=utf-8
#-*-encoding:cp936-*-
from functools import reduce
print("阿基米德");
r = list(map(str,[1,2,3,4,5,6,7,8,9]))
print(r)
def add(x,y):
	return x + y
sum = reduce(add,[1,2,3,4,5,6,7,8,9])
print(sum)
def is_odd(n):
	return n % 2 == 1
r = list(filter(is_odd,[1,2,3,4,5,6,7,8,9,10]))
print(r)
r = sorted([36,5,-12,9,-21])
print(r)
t = sorted([36,5,-12,9,-21],key = abs)
print(t)
lists = [36,5,-12,9,-21]
print(lists)
def i_abs(x):
	for x in lists:
		if x > 0:
			return x
		else:
			return -x
r = i_abs(lists)
print(r)
def calc_sum(*args):
	ax = 0
	for n in args:
		ax += n
	return ax
r = calc_sum(1,3,5,7,9)
print(r)
def lazy_sum(*args):
	def sum():
		ax = 0
		for n in args:
			ax += n
		return ax
	return sum
f = lazy_sum(1,3,5,7,9)
print(f())
f1 = lazy_sum(1,3,5,7,9)
f2 = lazy_sum(1,3,5,7,9)
print(f1 == f2)
print(f1() == f2())
def count():
	def f(j):
		def g():
			return j * j
		return g
	fs = []
	for i in range(1,4):
		fs.append(f(i))
	return fs
f1,f1,f3 = count()
print(f1(),f1(),f3())

r = list(map(lambda x: x * x, [1,2,3,4,5,6,7,8,9]))
print(r)
f = lambda x: x*x
print(f,f(20))
def now_time():
	print('2017-5-5')
f = now_time
f()
print(now_time.__name__,f.__name__)
def log(func):
	def wrapper(*args,**kw):
		print('call %s():'%func.__name__)
		return func(*args,**kw)
	return wrapper
@log
def now():
	print('2017-5-5')
now()
def log(text):
	def decorator(func):
		def wrapper(*args,**kw):
			print('%s %s():'%(text,func.__name__))
			return func(*args,**kw)
		return wrapper
	return decorator
@log('execute')
def now():
	print('2017-5-5')
now()
print(int('1234456',base = 8))
print(int('1234456',base = 10))
print(int('1234456',base = 16))

def int2(x,base = 2):
	return int(x, base)
print(int2('10000000'))
print(int2('101010010'))
