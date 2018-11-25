# coding = "utf-8"

import urllib.request
import re
import os
import requests

# open the url and read
def getFile(url):
    page = urllib.request.urlopen(url)
    f = open("diezhongdie.mp4","wb")
    block_sz = 8192
    while True:
        buffer = page.read(block_sz)
        if not buffer:
            break
        f.write(buffer)
    f.close()
def getRequestsFile(url):
    response = requests.get(url)
    print(response.status_code)

if __name__ == "__main__":
    url = "http://www.chinamoney.com.cn/dqs/cm-s-notice-query/fileDownLoad.do?contentId=1004106&priority=0&mode=save"
    url = "http://www.wudiyyw.com/3e6d0d25-df21-485e-9aaa-d9c0f5ba05e6"
    url = "http://87bo.cc/51fd36af-e2d9-43dd-bf01-4f02d93915bb"
    getFile(url)
    # getRequestsFile(url)