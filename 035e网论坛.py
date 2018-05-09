from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()
def getlinks(pageurl):

    global pages
    html = urlopen('http://www.e0575.cn/' + pageurl)
    bsobj = BeautifulSoup(html, 'lxml')
    try:
        print(bsobj.find(id='subject_tpc').text[:-7])
        print(bsobj.findAll(class_='readName b')[0].a.text)
        print(bsobj.findAll(class_='tipTop s6')[0].findAll('span')[1].text)
    except AttributeError:
        print('页面缺少一些属性')
    for link in bsobj.findAll('a', href = re.compile('^(read.php\?)tid\=.+')):
        if link.attrs['href'] not in pages:
            newpage = link.attrs['href']
            print('http://www.e0575.cn/'+newpage+'\n'+'----------------------------------------------------\n')
            pages.add(newpage)
            getlinks(newpage)

getlinks("")
