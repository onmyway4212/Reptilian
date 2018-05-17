from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()
def getlinks(pageurl):
    global pages
    html = urlopen('http://www.e0575.cn/' + pageurl)
    bsobj = BeautifulSoup(html, 'lxml')
    try:
        for title in bsobj.findAll('a', href=re.compile('read\.php\?tid=[0-9]+$')):
            print(title.get_text())
    except AttributeError:
        print('页面缺少一些属性')
    for link in bsobj.findAll('a', href = re.compile('^thread\.php')):
        if link.attrs['href'] not in pages:
            newpage = link.attrs['href']
            print('--------------------------------------------\n'+ 'http://www.e0575.cn/' + newpage)
            pages.add(newpage)
            getlinks(newpage)

getlinks("")

