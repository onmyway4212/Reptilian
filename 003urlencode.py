import urllib
import urllib.parse

def print_list(list):
    list = dir(urllib.parse)
    for each in list:
        print(each)

def urlencode():
    parms = {'score':100,'name':'爬虫基础','comment':'very good'}
    qs = urllib.parse.urlencode(parms)
    print(qs)
    print(urllib.parse.parse_qs(qs))

def parse_qs():
    url = 'https://www.baidu.com/s?wd=python%20%E6%9F%A5%E6%89%BE%E6%A8%A1%E5%9D%97%E7%9A%84%E5%B1%9E%E6%80%A7&rsv_spt=1&rsv_iqid=0xe93b6e7a00025be4&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&rqlang=cn&tn=baiduhome_pg&rsv_enter=1&oq=%25E7%2581%25AB%25E8%25BD%25A6%25E7%25A5%25A8&rsv_t=e9bf7OLgHzesdpcwBL%2F5TlY4zVi107VeFamqQttE%2F1Hou%2FLGBM3g9%2FZ1OCCM44%2Bv9QKZ&inputT=31786&rsv_pq=a071d85400027a25&rsv_sug3=57&rsv_sug1=62&rsv_sug7=100&rsv_sug2=0&rsv_sug4=31787'
    result = urllib.parse.parse_qs(url)
    print(result)

if __name__ == '__main__':
    parse_qs()

