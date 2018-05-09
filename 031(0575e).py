from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('http://www.e0575.cn/')
bsobj = BeautifulSoup(html, 'lxml')

'''
for link in bsobj.find('div', {'id': 'bodyContent'}).findAll('a', href= re.compile('^(/wiki/)((?!:).)*$')):
    if 'href' in link.attrs:
        print(link.attrs['href'])
'''
for link in bsobj.findAll('a', href = re.compile(r'thread\.php\?fid.?')):
    if 'href' in link.attrs:
        print(link.attrs['href'])
