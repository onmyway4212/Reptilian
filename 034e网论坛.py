from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()
def getlinks(pageurl):
    global pages
    html = urlopen('http://www.e0575.cn/' + pageurl)
    bsobj = BeautifulSoup(html, 'lxml')
    for link in bsobj.findAll('a', href = re.compile('^(read.php\?)tid\=.+')):
        if link.attrs['href'] not in pages:
            newpage = link.attrs['href']
            print('http://www.e0575.cn/'+ newpage)
            pages.add(newpage)
            getlinks(newpage)


getlinks("")
