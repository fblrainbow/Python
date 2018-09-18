#!/usr/bin/env python
#coding=utf-8
#__author__ = 'Administrator'
import requests

def get_json():
    r = requests.get('http://api.github.com/events')
    print(r.status_code)
    print(r.headers)
    print(r.text)
    print(r.content)
    print(r.json())

def get_quertString():
    url = 'http://httpbin.org/get'    #用来查看本机的信息
    params = {'qs1':'value1','qs2':'value2'}
get_json()
