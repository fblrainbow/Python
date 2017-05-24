#!/usr/bin/env python
#-*-coding:utf-8-*-
L = [x*x for x in range(10)]
print L
g = (x*x for x in range(10))
print g
print g.next()
print g.next()
print g.next()
for n in g:
	print n
def fib(max):
	n,a,b = 0,0,1
	while n < max:
		yield b
		a,b = b,a+b
		n = n+1
print fib(6)
