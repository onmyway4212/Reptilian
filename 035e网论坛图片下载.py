from urllib.request import urlopen
from urllib.request import urlretrieve
from bs4 import BeautifulSoup
import re
import os


pages = set()
def getlinks(pageurl):
    global pages
    html = urlopen('http://www.e0575.cn/' + pageurl)
    bsobj = BeautifulSoup(html, 'lxml')

    try:
        for imgurl in bsobj.findAll('img', src=re.compile(r'^http://img\.e0575\.com/attachment/Day_.+?')):
            print(imgurl['src'])
            path = imgurl['src'].split('/')[-1].split('?')[0]
            picPath = 'D:/pic/'+path
            if not os.path.exists('D:/pic'):
                os.makedirs('D:/pic')
            else:
                urlretrieve(imgurl['src'], picPath)
                print("%s已下载完成!" % picPath)


    except AttributeError:
        print('页面缺少一些属性')
    for link in bsobj.findAll('a', href = re.compile('read\.php\?tid=[0-9]+$')):
        if link.attrs['href'] not in pages:
            newpage = link.attrs['href'].split('/')[-1]
            print('--------------------------------------------\n'+ 'http://www.e0575.cn/' + newpage)
            pages.add(newpage)
            getlinks(newpage)



getlinks("thread.php?fid=131")
