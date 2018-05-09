import requests
from bs4 import BeautifulSoup
import os
import time
import re
import threading

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0',
            'Referer': 'http://www.mzitu.com'}


#这个头作为破解盗链使用
picreFerer = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0',
              'Referer': 'http://i.meizitu.net'}


#获得图集最大页数和名称
def get_page_name(url):
    html = get_html(url)
    soup = BeautifulSoup(html, 'lxml')
    span = soup.findAll('span')
    title = soup.find('h2', class_='main-title')
    return span[10].text, title.text


#获得页面html代码
def get_html(url):
    req = requests.get(url, headers=headers)
    html = req.text
    return html


def get_img_url(url):
    html = get_html(url)
    soup = BeautifulSoup(html, 'lxml')
    img_url = soup.find('div', {'class': 'main-image'}).find('img')
    return img_url['src']


#保存图片
def save_img(img_url, count, name):
    req = requests.get(img_url, headers=picreFerer, allow_redirects=False)    #allow_redirects=False 禁止用301重定向
    if not os.path.exists('D:/%s' % name):
        os.mkdir('D:/%s' % name)
    with open('D:/'+name+'/'+str(count)+'.jpg', 'wb') as f:
        f.write(req.content)

'''
def change_url(url):
    html = get_html(url)
    soup = BeautifulSoup(html, 'lxml')
    page_url = soup.find('a', href = re.compile(r'http://www.mzitu.com/[0-9]+?'))
    return page_url
'''


def main():
    old_url = 'http://www.mzitu.com/54625'
    page, name = get_page_name(old_url)             #通过函数的返回值赋值
    for i in range(1, int(page)+1):
        url = old_url+'/'+str(i)
        img_url = get_img_url(url)
        save_img(img_url, i, name)
        print('保存第'+str(i) + '张图片成功')
        time.sleep(1)
