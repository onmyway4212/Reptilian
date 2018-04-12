from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('https://baike.baidu.com/item/%E7%8C%AA%E5%85%AB%E6%88%92/769')
bsobj = BeautifulSoup(html, 'lxml')
for link in bsobj.find('div', {'class': 'content-wrapper'}).findAll('a', href= re.compile('^(/item/)((?!:).)*$')):
    if 'href' in link.attrs:
        print('https://baike.baidu.com'+link.attrs['href'])

