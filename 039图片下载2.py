from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup
import os

html = urlopen('https://tieba.baidu.com/p/5621153801?pn=1')

def Schedule(blocknum, blocksize, totalsize):
    '''
    :param blocknum:  已经下载的数据块
    :param blocksize: 数据块的大小
    :param totalsize: 远程文件的大小
    :return:
    '''
    per = 100.0 * blocknum * blocksize / totalsize
    if per > 100:
        per = 100
    print('当前下载进度: %d' %per)


bsobj = BeautifulSoup(html,'lxml')
images = bsobj.findAll('img',{'class': 'BDE_Image'})
i = 1
for image in images:
    if not os.path.exists('D:/pic'):
        os.makedirs('D:/pic')
    else:
        urlretrieve(image['src'],'D:/pic/a%s.jpg' % i , Schedule)
        print("a%s.jpg已下载完成!" % i)
        i+=1
