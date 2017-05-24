#!/sur/bin/env python
#-*-coding:utf-8-*-
def prod(x,y):
	return x*y
print reduce(prod,range(1,5))

def sushu(s):
	for n in range(2,s):
		if s % n == 0:
			return True
	return False
L = filter(sushu,range(2,101))
print L

