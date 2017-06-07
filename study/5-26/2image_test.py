#!/usr/bin/env python 
#-*-coding:utf-8-*-
import Image,ImageFilter
 
im = Image.open('example.png')
im2 = im.filter(ImageFilter.BLUR)

im2.save('2example_filter_blur.png','png')
