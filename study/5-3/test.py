#!/usr/bin/pytnon3
#encoding=utf-8
#-*-coding:cp936-*-

def fact(n):
	if n == 1:
		return 1
	return n * fact(n-1)
print (fact(5))
L = []
n = 1
while n <= 99:
	L.append(n)
	n += 2
#for i in range(99):
print(L)
S = ['Michael','Sarah','Tracy','Bob','Jack']
print(S[0],S[1],S[2])
r = []
n = 3
for i in range(n):
	r.append(S[i])
print(r)
print(S[:4])
print(L[::5])
d = {'a':1,'b':2,'c':3}
#for key in d:
#	print(key)
for value in d.values():
	print(value)
for k,v in d.items():
	print(k,v)
from collections import Iterable
print(isinstance('abc',Iterable))
print(isinstance([1,2,3,4,5],Iterable))
print(list(range(1,50)))
C = [x*x for x in range(1,10)]
print(C)
C = [ m + n + l +o for m in 'ABC' for n in 'XYZ' for l in '123' for o in '#$^']
print(C)
d = {'x':'a','y':'b','z':'c'}
for k,v in d.items():
	print(k,'=',v)
L = 



























































