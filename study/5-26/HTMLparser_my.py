#!/usr/bin/env python
#-*-coding:utf-8
from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint

class MyHTMLParser(HTMLParser):
	def handle_starttag(self, tag, attrs):
		print ('<%s>' %tag)
	
	def handle_endtag(self,tag):
		print ('</%s>' %tag)

	def handle_startendtag(self, tag, attrs):
		print ('<%s/>' %tag)
	
	def handle_data(self,data):
		print ('data')

	def handle_comment(self,data):
		print ('<!-- -->')
	
	def hand_entityref(self,name):
		print ('&%s;' %name)

	def hand_charref(self, name):
		print ('&#%s;' %name)

parser = MyHTMLParser()
print parser.feed('<!DOCTYPEhtml><htmllang="zh-cn"><head><basehref="http://www.kanxue.com/"/><!--{hookheader_mete_before.htm}--><metahttp-equiv="X-UA-Compatible"content="IE=Edge,chrome=1"><title>看雪学院</title><!--{hookheader_link_after.htm}--></head><body><!--{hookheader_body_start.htm}--></body></html>')
