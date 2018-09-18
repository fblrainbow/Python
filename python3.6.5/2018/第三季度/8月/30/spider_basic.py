import urllib.request
import urllib.parse
import urllib.error



def print_list(list):
    for i in list:
        print(i)
def demo(url):
    s=urllib.request.urlopen(url)
    # print(s.close())
    for i in range(10):
        print('line %s:%s '%(i+1,s.readline()))
        # s.readlines()   这个方法返回的是一个列表list
    print_list(s.readlines())
    # print('返回码是：%s' %s.getcode())
def urlencode():
    params = {'score':100,'name':'爬虫基础','comment':'very good'}
    qs = urllib.parse.urlencode(params)
    print(qs)
    # t = '中文转换字符串'
    # print(urllib.parse.quote(t),urllib.parse.unquote(t))
def down_load_stock_data(stock_list):
        for sid in stock_list:
            url='https://datacenter.jin10.com/reportType/dc_usa' + sid
            fname = sid + '.reportType'
            print('downloading %s form %s' %(fname,url))
            urllib.request.urlretrieve(url,fname)


def request_post_debug():
    data = {'username':'fwp','password':'xxxxxxxxxx'}
    headers = {'User-Agent':'Mozilla/5.0'}
    req = urllib.request('http://www.douban.com',data=urllib.parse.urlencode(),headers=headers)
    s = urllib.urlopen(req)
    # print(s.read(100))
    s.close()

if __name__ == '__main__':
    stock_list = ['_gdp','_cpi','_unemployment_rate']
    url = 'https://datacenter.jin10.com/reportType/dc_usa_gdp'
    request_post_debug()
    # down_load_stock_data(stock_list)
