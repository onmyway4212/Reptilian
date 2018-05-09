import urllib
import urllib.request
import urllib.error
import re
import itertools
import time

#下载网页函数，错误代码500多时服务器端的问题，我们尝试重新下载2次
def download(url, user_agent='wswp', num_retries=2):
    print('downloading url: %s' % url)
    headers = {'User-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0'}
    request = urllib.request.Request(url, headers=headers)
    try:
        html = urllib.request.urlopen(request).read()
    except urllib.error.URLError as e:
        print('downloading error:', e.reason)
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:            #当错误代码在500多到600之间时，重新返回函数再执行
                return download(url, user_agent, num_retries-1)
    return html


def crawl_sitemap(url):
    sitemap = download(url)
    links = re.findall(r'<loc>(.*?)</loc>', sitemap)
    for link in links:
        html = download(link)

crawl_sitemap('http://127.0.0.1:8000/places/default/sitemap.xml')