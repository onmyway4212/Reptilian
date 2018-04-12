from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()
def getlinks(pageurl):
    global pages
    html = urlopen('https://baike.baidu.com' + pageurl)
    bsobj = BeautifulSoup(html, 'lxml')
    for link in bsobj.findAll('a', href = re.compile('^(/item/)')):
        if link.attrs['href'] not in pages:
            newpage = link.attrs['href']
            print('https://baike.baidu.com'+ newpage)
            pages.add(newpage)
            getlinks(newpage)


getlinks("")
