#!/usr/bin/python3
#encoding=utf-8
#-*-encoding:cp936-*-
L = [ x*x for x in range(10)]
print(L)
g = ( x *x for x in range(10))
print(g)
for n in range(10):
	print(next(g))
def fib(max):
	n,a,b = 0,0,1
	while n < max:
		a,b = 
