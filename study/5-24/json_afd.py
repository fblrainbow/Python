#!/usr/bin/env python 
#-*-coding:utf-8-*-
import json
'''
d = dict(name = 'Bob',age = 20,score = 88)
L = json.dumps(d)
print L
json_str = '{"age":20,"score":88,"name":"Bob"}'
L = json.loads(json_str)
print L
'''
class Student(object):
	def __init__(self,name,age,score):
		self.name = name
		self.age = age
		self.score = score
s = Student('Bob',20,88)
def student2dict(std):
	return {
		'name':std.name,
		'age':std.age,
		'score':std.score
		}

print json.dumps(s,default=student2dict)
