#coding:utf-8
import urllib
def getHtmlCode(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html