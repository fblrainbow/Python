# coding = UTF-8
# 爬取李东风PDF文档,网址：http://www.math.pku.edu.cn/teachers/lidf/docs/textrick/index.htm

import urllib.request
import re
import os

# open the url and read
def getFile(url):
    page = urllib.request.urlopen(url)
    f = open("demo.xlsx","wb")
    block_sz = 8192
    while True:
        buffer = page.read(block_sz)
        if not buffer:
            break
        f.write(buffer)
    f.close()

if __name__ == "__main__":
    url = "http://www.math.pku.edu.cn/teachers/lidf/docs/textrick/tricks.pdf"
    url = "http://dt.80txt.com/556/%E7%9B%98%E9%BE%99.txt"#盘龙
    url = "http://www.chinamoney.com.cn/dqs/cm-s-notice-query/fileDownLoad.do?contentId=1004106&priority=0&mode=save"#盘龙

    getFile(url)
