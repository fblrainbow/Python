#!#!/usr/bin/env python
#coding:utf-8
from model.html import get_info

cookies = {
	'cookie':'thw=cn; v=0; cna=MkTXE5WKYD8CATo+XZdEAy4d; t=0443eaf5fb0ca14592ad33526d8d55a8; cookie2=101422f0d8d301c61c9d517d49690560; _tb_token_=5e743833b7903; unb=1838150518; sg=%E6%9E%978d; _l_g_=Ug%3D%3D; skt=e22463a2d24e6158; cookie1=AnPIF0%2FkFA9bXMSS9f9%2FXgHJLE1cBD%2FQq6wXOeDUOZ0%3D; csg=42dc27e1; uc3=vt3=F8dBzrhAL3r%2BnaIjHNc%3D&id2=UonYuY92RZ%2Fi7w%3D%3D&nk2=tNDuIvM3BXEFMNPE&lg2=W5iHLLyFOGW7aA%3D%3D; existShop=MTUzMjAxMDYxNA%3D%3D; tracknick=%5Cu7D2B%5Cu8F69love%5Cu679A%5Cu6797; lgc=%5Cu7D2B%5Cu8F69love%5Cu679A%5Cu6797; _cc_=URm48syIZQ%3D%3D; dnk=%5Cu7D2B%5Cu8F69love%5Cu679A%5Cu6797; _nk_=%5Cu7D2B%5Cu8F69love%5Cu679A%5Cu6797; cookie17=UonYuY92RZ%2Fi7w%3D%3D; tg=0; mt=ci=43_1; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0; whl=-1%260%260%260; JSESSIONID=E774902B1002E8F004E06ECBBFA13E7F; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; uc1="cookie15=URm48syIIVrSKA%3D%3D"; hng=CN%7Czh-CN%7CCNY%7C156; swfstore=289099; isg=BGJi2nIeTe3pLVGxQ0hpYkD6pugEG2ep32CBS6z7HFXOfwL5lEO23eh1q_sm795l'
}		

headers = {
	'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.5702.400 QQBrowser/10.2.1893.400'
}

def get_img_list(html):
	tag_img_list = html.find_all('script') 
	# print('img list Count:',len(tag_img_list))
	# print(html)
	print(tag_img_list[7].get_text().replace('\n','').replace(' ','').split(';')[0])
	# print(tag_img_list[7].get_text().replace('\n','').replace(' ',''))

	# print(tag_img_list[7])

if __name__ == '__main__':
	url = 'https://s.taobao.com/search?q=%E6%89%8B%E6%9C%BA&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306'
	# url = 'https://s.taobao.com/search?spm=a230r.1.0.0.4e0a6fbe0e2VuG&q=%E6%89%8B%E6%9C%BA&spu_title=%E5%B0%8F%E7%B1%B3+%E5%B0%8F%E7%B1%B3%E6%89%8B%E6%9C%BA8&app=detailproduct&pspuid=1612229&cat=1512&from_pos=20_1512.default_0_1_1612229&spu_style=grid'

	# print(1)
	html = get_info(url,cookies,headers).get_html_tree()
	# print(2)
	get_img_list(html)
