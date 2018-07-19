
#!/usr/bin/env python
#coding:utf-8

import sys
import re
import time
from bs4 import BeautifulSoup
import requests
from model.html import get_key_info

url = 'https://blog.csdn.net/qq_37608398'
def save(filename,content):
	try:
		f = open(filename,'a+')
		f.write(content)
		f.close()
	except:
		f.close()
	finally:
		f.close()


if __name__ == '__main__':
	key_info = get_key_info(url)
	save(url.split('/')[-1] + '.txt',key_info)