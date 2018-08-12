#!/usr/bin/env python
#coding:utf-8

import re
import time
import requests
from bs4 import BeautifulSoup


class get_info():
	def __init__(self,url,cookies,headers):
		self.url = url
		self.cookies = cookies
		self.headers = headers

	def get_html_tree(self):
		response = requests.get(url = self.url,cookies = self.cookies,headers = self.headers)
		html = BeautifulSoup(response.text,'html.parser')
		return html