#!/usr/bin/env python
#coding=utf-8
#__author__ = 'Administrator'
class Animal(object):
    def run(self):
        print ('Animal is running...')
class Dog(Animal):
    def run(self):
        print('Dog is running...')
class Panda(Animal):
    def run(self):
        print('Panda is running...')
    def eat(self):
        print('Eating bamboo')
dog=Dog()
panda=Panda()
dog.run()
panda.run()
panda.eat()
def run_twice(animal):
    animal.run()
    animal.run()
run_twice(Panda())
class Tortoise(Animal):
    def run(self):
        print('tortoise is running slowly...')
a = Tortoise()
b = Tortoise()
run_twice(Tortoise())
class Timer(object):
    def run(self):
        print ('Start...')
run_twice(Timer())
# 判断一个变量是否是某个类型可以用isinstance()判断：
class Cat(Animal):
    pass
print(isinstance(Dog ,object))
print(isinstance(dog,Dog))
class object():
    pass
print (isinstance(dog,object))
# 获取对象信息的函数 type();isinstance();dir().其中 dir（）是获取一个对象的所有属性和方法
print(dir(Panda))