import requests
from bs4 import BeautifulSoup
import os
import re


url = 'http://www.dongqiudi.com/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0',
            'Referer': 'http://www.mzitu.com'}
list = []
html = requests.get(url, headers=headers)
bsobj = BeautifulSoup(html.text, 'lxml')
for r in bsobj.find('div', {'id': 'news_list'}).findAll('li'):
    t = r.h2.a
    print(t['href'])
    print(t.text)
