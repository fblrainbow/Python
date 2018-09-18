#!/usr/bin/env python
#coding=utf-8
#__author__ = 'Administrator'
from urllib import request
def download_stock_data(url):

        fname = 'fa.jpg'
        request.urlretrieve(url,fname)


if __name__ == '__main__':
    url = 'https://raw.githubusercontent.com/abidrahmank/OpenCV2-Python-Tutorials/master/data/left.jpg'
    download_stock_data(url)
    # http://table.finance.yahoo.com/table.csv?s=300001.sz