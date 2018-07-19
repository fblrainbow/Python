#/usr/bin/env pyton
#coding:utf-8

import time
from bs4 import BeautifulSoup
import requests

def get_key_info(url):
	response = requests.get(url = url)
	if 200 == response.status_code:
		pass
		# print(response.text)
	else:
		exit()
	get_code_tree = BeautifulSoup(response.text,'html.parser')
	tag_totle_key_info = get_code_tree.find('div',class_ = 'grade-box clearfix')
	tag_dd_key_info = tag_totle_key_info.find_all('dd')
	# print(tag_dd_key_info)
	# print(len(tag_dd_key_info))
	grade = tag_dd_key_info[0].a['title'].split(',')[0]
	access = tag_dd_key_info[1]['title']
	score = tag_dd_key_info[2]['title']
	rank = tag_dd_key_info[3].get_text()
	# print(type(grade),type(access),type(score),type(rank))
	content = 	'时间：' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n'\
				'博客等级：' + grade + '\n'\
				'访问量：' + access + '\n'\
				'积分：' + score + '\n'\
				'排名：' + rank + '\r\r\n'

	return content