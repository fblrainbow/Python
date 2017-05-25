#!/usr/bin/env python
#-*-coding:utf-8-*-
import time,threading
balance = 0
def change_it(n):
	global balance
	balance = balance + n
	balance = balance - n
lock = threading.Lock()

def run_thread(n):
	for i in range(10000):
		#先要获取锁：
		lock.acquire()
		try:
			#放心改吧
			change_it(n)
		finally:
			#free lock
			lock.release()
t1 = threading.Thread(target = run_thread,args = (5,))
t2 = threading.Thread(target = run_thread,args = (8,))
t1.start()
t2.start()
t1.join()
t2.join()
print balance
