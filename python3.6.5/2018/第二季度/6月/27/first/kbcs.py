#!/usr/bin/env python3
#coding=utf-8

def calc(*number):
	sum = 0
	for n in number:
		sum = sum + n * n
		print(sum)
	return sum
number = range(5)

print(calc(*number))