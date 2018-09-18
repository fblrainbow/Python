#!/usr/bin/env python
#coding=utf-8
#__author__ = 'Administrator'
# name = input("Input your name:")
#
# print(name)
# x = "中文"
# print(len(x))
# y = x.encode()
# print(len(y),y)
# x = 0.023
# print("%019f" %x)

'a test module'

# name = input('Please enter your name:')
# def _private_1(name):
#     	return 'Hello,%s' %name
# def _private_2(name):
#     	return 'Hi,%s' %name
# def greeting(name):
# 	try:
# 	name = input('Please enter your name:')
# 	if len(name) >= 3:
# 		return _private_1(name)
#     else:
#      	return  _private_2(name)
		
# 	except Exception as e:
# 		raise e




# if __name__ == '__main__':
# 	greeting(name)
# L=list['fwgjg\n  jfsfhaahfk-jjf\n  kfkfaf-ms\n']
#
# L = ['fshdsf','wsffsfsf']
# for i in L:
# 	for x in i:
# 		print(x)
# x ='help /login'
# y = 'lo' + x.split('lo')[1]
# print(y)
# def f(a):
# 	b = 9
# 	a = a+b
# 	print(a)
# print(f(4)
# A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
# A3 = [A0[s] for s in A0]
# A1 = range(10)
# A5 = {i:i*i for i in A1}
# for a in A5:
# 	TMP=(A5[a])
# 	print(TMP)
# print(A5)
# def f(i,l=[]):
# 	for x in range(i):
# 		l.append(x*x)
# 	print(l)
# print(f(2),f(3,[3,2,1]),f(3))
# class A():
# 	def go(self):
# 		print ('go A go')
# class B(A):
# 	def go(self):
# 		super(B,self).go()
# 		print('go B go')
# class C(A):
# 	def go(self):
# 		super(C,self).go()
# 		print('go C go')
# class D(B,C):
# 	def go(self):
# 		super(D,self).go()
# 		prin('go D go')
# class E(B,C):
# 	pass

# print(a,b,c,d,e = A(),B(),C(),D(),E())
import random
i = 1
a = random.randint(0,100)
print(a)
b = int( input('请输入0-100中的一个数字：'))
while a!= b:
    if a > b:
        print('你第%d输入的数字小于电脑随机数字'%i)
        b = int(input('请再次输入数字:'))
    else:
        print('你第%d输入的数字大于电脑随机数字'%i)
        b = int(input('请再次输入数字:'))
    i+=1
else:
    print('恭喜你，你第%d次输入的数字与电脑的随机数字%d一样'%(i,b))
