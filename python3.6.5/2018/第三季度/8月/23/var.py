#!/usr/bin/env python
#coding=utf-8
#__author__ = 'Administrator'
# print("Hello World!")
# name = "fbl"
# name1 = name
# print(name,name1)
# 姓名 = "fbl"
# print(姓名)
name = input("Name:")
age = input("Age:")
job = input("Job:")
salary = input("Salary:")

info = '''
---- Info of %s ----
Name:%s
Age:%s
Job:%s
Salary:%s
---- End ----
'''%(name,name,age,job,salary)


info2 = '''
---- Info of {0} ----
Name:{0}
Age:{1}
Job:{2}
Salary:{3}
---- End ----
'''.format(name,age,job,salary)

info3 = '''
---- Info of {_name} ----
Name:{_name}
Age:{_age}
Job:{_job}
Salary:{_salary}
---- End ----
'''.format(_name = name,_age = age,_job = job,_salary = salary)


print(info3)
