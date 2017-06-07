#!/usr/bin/env python 
#-*-coding:utf-8-*-
import Image, ImageDraw, ImageFont, ImageFilter

#random char 
def rndChar():
	return chr(random.radint(65, 90))

#random color
def rndColor():
	return (random.randint(64, 255),random.randint(64, 255), random.randint(64, 255))

#random color2
def rndColor2():
	return (random.randint(32, 127),random.randint(32, 127), random.randint(32, 127))

width = 240
height = 60
