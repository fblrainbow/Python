#!/usr/bin/env python
#coding=utf-8
#__author__ = 'Administrator'
import requests
from html.parser import HTMLParser


class DoubanClient():
    def __init__(self):
        headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
            'Origin':'https://www.douban.com'
        }
        self.session = requests.Session()
        self.session.headers.update(headers)
    def login(self,username,password,source='index_nav',redir='http://www.douban.com/',login='登录'):
        url = 'https://www.douban.com/accounts/login'
        data = {
            'form_email':username,
            'form_password':password,
            'source':source,
            'redir':redir,
            'login':login
        }
        headers ={
        'referer':'https://www.douban.com/accounts/login?source=main',
        'host':'accounts.douban.com'
        }
        self.session.post(url=url,data=data,headers=headers)
        print(self.session.cookies.items())


if __name__ == '__main__':
    fbl = DoubanClient()
    fbl.login('846058904@qq.com','FBLATPX4869@')