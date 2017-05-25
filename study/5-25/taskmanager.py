#!/usr/bin/env python
#-*-coding:utf-8-*-
#taskmanager.py
import random,time,Queue
from multiprocessing.managers import BaseManager

#TXqueue
task_queue = Queue.Queue()

#RXqueue
result_queue =Queue.Queue()

#from BaseManager to QueueManager:
class QueueManager(BaseManager):
	pass

#take the Queue register to network,callable 
QueueManager.register('get_task_queue',callable = lambda:task_queue)
QueueManager.register('get_result_queue',callable = lambda:result_queue)

#bind port 5000,set passwd'fbl':
manager = QueueManager(address = ('',5000),authkey='fbl')

#launch Queue:
manager.start()

#get network Queue object
task = manager.get_task_queue()
result = manager.get_result_queue()

#set a series of task in:
for i in range(10):
	n = random.randint(0,10000)
	print ('Put task %d...' %n)
	task.put(n)


#read result from result-queue:
print('Try get result...')
for i in range(10):
	r = result.get(timeout = 20)
	print('Result: %s' %r)


#close:
manager.shutdown()


