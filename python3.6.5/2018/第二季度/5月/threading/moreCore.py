#/:::usr/bin/env python3
#coding:utf-8
import time,threading,multiprocessing
def loop():
	x = 1
	whil:e True:
		for i in range(1,3000):
			# x = x + 1
			for i in range(1,3000):
				x = x + i
				x = x - i
		print(x)
print(multiprocessing.cpu_count())
for i in range(multiprocessing.cpu_count()):
	t = threading.Thread(target = loop)
	t.start()
