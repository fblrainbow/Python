#!/usr/bin/env python
#-*-coding:utf-8-*-

class Animal(object):
	def run(self):
		print 'Animal is running...'
class Dog(Animal):
	pass
class Cat(Animal):
	pass
dog = Dog()
cat = Cat()
print dog.run(),cat.run()

def run_twice(animal):
	animal.run()
	animal.run()
print run_twice(Animal())
print run_twice(Dog())
