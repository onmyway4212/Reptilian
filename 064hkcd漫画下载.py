from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup
import os
import threading
import random

if not os.path.exists('d:\\xkcd\\'):
    os.mkdir('d:\\xkcd\\')
os.chdir('d:\\xkcd\\')


def download(start, end):
    for urlNumber in range(start, end):
        if urlNumber == 404:
            return
        html = urlopen('http://xkcd.com/%s' % (urlNumber))
        bsobj = BeautifulSoup(html, 'lxml')
        soup = bsobj.find('div', {'id': 'comic'}).find('img')['src']
        if soup == []:
            print('找不到这一页的图像！')
        else:
            name = soup.split('/')[-1]
            soup = 'http:' + soup
            urlretrieve(soup, name)
            print('%s已经下载完成！' % (name))

            soup2 = bsobj.findAll('a',{'rel' : 'prev'})[0]
            comicUrl = 'https://xkcd.com' + soup2['href']
            html = urlopen(comicUrl)


downloadTreads = []

#每一次for循环创建一个线程
for i in range(1, 1400, 100):
    downloadTread = threading.Thread(target=download, args = (i, i+99))
    downloadTreads.append(downloadTread)
    downloadTread.start()

for downloadTread in downloadTreads:
    downloadTread.join()
print('Done.')