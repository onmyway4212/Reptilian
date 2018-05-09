from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()
def getlinks(pageurl):
    global pages
    html = urlopen('https://en.wikipedia.org' + pageurl)
    bsobj = BeautifulSoup(html, 'lxml')
    for link in bsobj.findAll('a', href=re.compile('^(/wiki/).+')):
        if link.attrs['href'] not in pages:
            newpage = link.attrs['href']
            print('https://en.wikipedia.org'+ newpage)
            pages.add(newpage)
            getlinks(newpage)

getlinks("")
