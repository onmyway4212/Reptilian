import urllib.request
import re


def open_url(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')
    page = urllib.request.urlopen(req)
    html = page.read().decode('utf-8')
    return html


def get_img(html):
    # 正则表达式表示IP地址
    # p1 = r'(([01]?\d?\d|2[0-4]\d|25[0-5])\.){3}([01]?\d?\d|2[0-4]\d|25[0-5])'

    p2 = r'(?:(?:[01]?\d?\d|2[0-4]\d|25[0-5])\.){3}(?:[01]?\d?\d|2[0-4]\d|25[0-5])'

    # imglist1 = re.findall(p1, html)
    imglist2 = re.findall(p2, html)

    for each in imglist2:
        print(each)


if __name__ == '__main__':
    url = 'https://www.kuaidaili.com/free/inha/'
    get_img(open_url(url))
