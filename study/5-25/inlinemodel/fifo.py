#!/usr/bin/env python
#-*-coding:utf-8-*-
from collections import OrderDict
class LastUpdateOrderedDict(OrderDict):
	def __init__(self,capacity):
		super(LastUpdateOrderedDict,self).__init__()
		self._capacity = capacity
	def __setitem__(self,key,value):
		containsKey = 1 if key in self else 0
		if len(self) - containsKey >= self._capacity:
			last = self.popitem(last = False)
			print 'remove:',last
		if containsKey:
			del self[Key]
			print 'set:',(key,value)
		else:
			print 'add:',(key,value)
	OrderDict.__setitem__(self,key,value)
