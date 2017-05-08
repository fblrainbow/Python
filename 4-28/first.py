#!/usr/bin/python3
#coding=utf-8
#-*-coding:cp936-*-

import math

print ('hello,horld')

print(100+200)
print('The quick brown fox','jumps over','the lazy dog')
print('100 + 200 =',100+200)
#name = input()
#print name
#yourname = input('please enter your name:')
#print 'hello,',yourname
#print
a = 100
if a >= 0:
	print(a)
else:
	print(-a)
print('I\'m ok.')
print(r'\t\\t\\\\t')
print('''jlimenjj
sfasdfasf
sfafsdffda
''')
print(True,3 > 4, 3 > 1)
print(3 > 2 and 5 > 3)
print(3 > 5 or 3 > 4)
print(not 3 < 5)
print(10 / 3, 10.0 / 3,9 / 3,10 // 3,10 % 3)
print(u'请输入')
print(ord('a'),ord('中'))
'''name = input("请输入：")
print('hello',name)
'''
print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))
print(b'ABC'.decode('ascii'))
print(b'\xe3\xb8\xad\xe6\x96\x87'.decode('utf-8'))
print('中文'.encode('gb2312'))
print(len(b'ABC'))
print('%-2d-%02d' %(3,1))
print('%.2f' % 3.1415926)
print('Age:%s.Gender:%s'%(25,True))
print('growth rate:%d%%' % 7)
s1 = 72
s2 = 85
r = (85 - 72) * 100 / 72
print('%2.1f%%'% r)

#list 列表	
classmates = ['Michael','Bob','Tracy']
print(classmates,len(classmates),classmates[0],classmates[1],classmates[2])
classmates.append('fbl')
print(classmates)
classmates [-1] = 'sfs'
classmates.insert(1,'jack')
print(classmates)
tanchu = classmates.pop()

print(tanchu)
print(classmates)
tanchu1 = classmates.pop(2)
print(tanchu1)

print(classmates)
L = ['Apple',123,True]
S = [ L,'sdf','dsf' ]
print(len(L),len(S))
	
#tuple 元组
classmates = ('Micheal','Bob','Tracy')
print(classmates[0])
# classmates[0] ='dfs' tuple object doesn't support item assignment!
t = (1,2)
print(t)
t = ()
print(t)
t = (1)  
print(t)
t = (1,)
print(t)
t = ('a','b',['A','B'])
print(t)
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)



#条件判断
age = 20;
if age >= 18:
	print('You age is',age)
	print('adult')
age =int ( input('请输入你的年龄：'))
if age >= 18:
	print('You age is',age)
	print('adult')
elif age >= 6:
	print('You age is',age)
	print('teenager')
else:
	print('kid')



# 循环
names = ['Michael','Bob','Tracy']
for name in names:
	print(name)

sum = 0;
i = 0;
for i in range(101):
	sum+=i
print(sum)


names = ['Michael','Bob','Tracy']
scores = [95,75,85]

d ={'Michael':95,'Bob':75,'Tracy':85}
print(d['Michael'])
s = 'Bob' in d
print(s)
print(d.get('Tracy'))
print(d.get('dfk',-1))
print(d.pop('Bob'))
print(d)
t = set([1,2,3,1,4,5,2])
print (t)
t.add(6)
t.remove(2)
print(t)
s1 = set ([1,2,3,8])
s2 = set ([2,5,8])
print(s1 & s2,s1 | s2)
a = ['c','b','a']
print(a)
a.sort()
print(a)
n1 = 255
print(hex(n1))

def my_abs(x):
	if x >= 0:
		return x
	else:
		return -x
def nop():
	pass
if age >= 18:
	pass
print(my_abs(-21))


def move(x,y,step,angle = 0):
	nx = x + step*math.cos(angle)
	ny = y + step*math.sin(angle);
	return nx,ny
r=(x,y) = move(100,100,60,math.pi / 6)
print(x,y)
print(r)
print(math.sqrt(3))
