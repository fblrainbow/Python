#!/usr/bin/env python
#coding=utf-8
#__author__ = 'Administrator'
# class Man(object):
#     def __init__(self, name, gender):
#         self.name = name
#         self.__gender = gender
#     def get_gender(self):
#         return self.__gender
#     def set_gender(self,gender):
#         self.__gender=gender
# bart = Man('Bart', 'male')
# if bart.get_gender() != 'male':
#     print('测试失败!')
# else:
#     bart.set_gender('female')
#     if bart.get_gender() != 'female':
#         print('测试失败!')
#     else:
#         print('测试成功! The sex of Bart is %s' %bart._Man__gender)

class Student(object):
    def __init__(self,name,score):
        self.name=name
        self.__score=score
    def get_score(self):
        return self.__score
    def set_score(self,score):
        if 0 <= score <= 100:
            self.__score=score
        else:
            raise ValueError('bad score!')
#测试
Lisa=Student('lisa',-10)
print('Her name is %s and her score is %d ' %(Lisa.name,Lisa.get_score()))
