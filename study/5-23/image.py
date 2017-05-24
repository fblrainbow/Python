#!/usr/bin/env python
#-*-coding:utf-8-*-
import Image
im = Image.open('aaa_test.png')
print im.format,im.size,im.mode 
im.thumbnail((1700,860))
im.save('thumb.jpg','JPEG')
