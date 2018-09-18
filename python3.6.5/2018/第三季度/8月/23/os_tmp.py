#!/usr/bin/env python
#coding=utf-8
#__author__ = 'Administrator'
import os
res = os.popen("dir").read()

print(res)