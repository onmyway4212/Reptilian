from urllib.request import urlopen
from urllib.request import urlretrieve
from bs4 import BeautifulSoup
import re

pages = set()


def getLinks(pageUrl):
    global pages
    html = urlopen("http://www.meizitu.com/" + pageUrl)
    bsObj = BeautifulSoup(html, "html.parser")
    try:
        for url in bsObj.find(id='maincontent').findAll('img', src=re.compile(r'^http://mm.+\.jpg$')):
            url2 = url.attrs['src']
            print(url2)
            #filename = url2.split('/')[-4].replace('/', '_')
            #urlretrieve(url2, filename)
    except AttributeError:
        print("This page is missing something! No worries though!")

    for link in bsObj.findAll("a", href=re.compile(r'a/.+\.html$')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newPage = link.attrs['href'][23:]
                print("----------------\n" + newPage)
                pages.add(newPage)
                getLinks(newPage)


getLinks("")


#http://mm.chinasareview.com/wp-content/uploads/2017a/08/02/01.jpg
#http://www.meizitu.com/a/5591.html