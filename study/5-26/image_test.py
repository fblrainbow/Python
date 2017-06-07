#!/usr/bin/env python 
#-*-coding:utf-8-*-
import Image
 
im = Image.open('example.png')
w,h = im.size

im.thumbnail((w//2,h//2))
im.save('example_1.png','png')
