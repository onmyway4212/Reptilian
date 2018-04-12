from urllib.request import urlopen
from bs4 import BeautifulSoup
import urllib.parse
import re

pages = set()
def getlinks(pageurl):

    global pages
    html = urlopen('https://baike.baidu.com' + pageurl)
    bsobj = BeautifulSoup(html, 'lxml')
    try:
        #print(bsobj.find('',{'class': 'lemmaWgt-lemmaTitle-title'}).text)
        #print(bsobj.find(id='siteSub').text)
        print(1)
    except AttributeError:
        print('页面缺少一些属性')
    for link in bsobj.findAll('a', href = re.compile('^(/item/).+')):
        if link.attrs['href'] not in pages:
            newpage = link.attrs['href']
            newpage = urllib.parse.urlencode({'word':newpage})
            print('https://baike.baidu.com/item/'+newpage+'\n'+'----------------------------------------------------\n')
            pages.add(newpage)
            #getlinks(newpage)

getlinks("")
