#!/usr/bin/env python 
#-*-coding:utf-8-*-
from collections import namedtuple
Point = namedtuple('Point',['x','y'])
p = Point(1,2)
print p.x,p.y

Circle = namedtuple('Circle',['R','x','y'])
c = Circle(5,0,5)
print c.R,c.x,c.y

from collections import deque
q = deque(['a','b','c'])
q.append('x')
q.appendleft('y')
print q
