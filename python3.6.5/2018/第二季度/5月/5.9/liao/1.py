#coding:utf-8
# def fbl():
# 	print('2015-07-8')
# print(fbl.__name__)
# def log(func):
# 	def wrapper(*args,**kw):
# 		print('call %s():' %func.__name__)
# 		return func(*args,**kw)
# 	return wrapper
# @log
# # def now():
# 'test'
# 'safd'
# # print(__init__)
# __author__ = 'fanbinglin'
# 'af'
# """
# sfadfadf
# afadfaf
# afdsfaf
# """
# """ dfadfadfafa"""
# import sys
# def test():
# 	args = sys.argv
# 	if len(args) == 1:
# 		print('hello')
# 	elif len(args) == 2:
# 		print('hello,%s!'%args[1])
# 	else:
# 		print('too many arguments!')
# if __name__ == '__main__':
# 	test()
# print(__name__)
# # 	print('2015-3-25')
# # now()

# class student(object):
# 	def __init__(self,name,score):
# 		self.name = name
# 		self.score = score
# 	def print_score(self):
# 		print('%s:%s'%(self.name,self.score))
# bart = student('bsdf',59)
# lisa = student('lisa',86)
# bart.print_score()

# class student(object):
# 	def __init__(self,name,score):
# 		self.__name = name
# 		self.__score = score
# 	def print_score(self):
# 		print('%s:%s'%(self.__name,self.__score))
# bart = student('bsdf',59)
# lisa = student('lisa',86)
# bart.print_score()
# bart.name='ql'
# print(bart._student__name)
# def fn():
# 	pass
# class animo(object):
# 	def run(self):
# 		print("animo is runing!")
# class Dog(animo):
# 	def run(self):
# 		print("Dog is runing")

# class cat(animo):
# 	def run(self):
# 		print("Cat is running")
# dog = Dog()
# dog.run()
# Cat = cat()
# Cat.run()


# print(isinstance(dog,cat))
# print(type(fn))
# print(type(abs))


class Student(object):
	name = 'Student'
s = Student()
print(s.name)
s.name = 'qml'
s.name = 'fbl'
print(s.name)
del s.name
print(s.name)