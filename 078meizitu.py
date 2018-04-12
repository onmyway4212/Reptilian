import requests
from bs4 import BeautifulSoup
import re
import os
import time
import threading



headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0',
            'Referer': 'http://www.mzitu.com'}

#startTime = time.time()
img_folder = 'd:\\meizitu2\\'
if not os.path.exists(img_folder):
    os.mkdir(img_folder)
os.chdir(img_folder)


def load(newUrl):
    html=requests.get(newUrl, headers=headers)
    bsobj = BeautifulSoup(html.text, 'lxml')
    downloadPic(bsobj)

def getUrl(i):
    url = 'http://www.meizitu.com/a/'+str(i)+'.html'
    html = requests.get(url, headers=headers)
    bsobj = BeautifulSoup(html.text, 'lxml')
    for newUrl in bsobj.findAll('a', href = re.compile(r'http://www.meizitu.com/a/[0-9]+?\.html')):
        print(newUrl['href'])
        load(newUrl['href'])





def downloadPic(bsobj):
    for link in bsobj.find('div',{'id': 'maincontent'}).findAll('img', src = re.compile(r'http://mm.chinasareview.com/wp-content/uploads.+?\.jpg')):
        link = link['src']
        html2= requests.get(link, headers=headers)
        picName2 = link.split('/')[-4:]                                      #把列表转化成字符串
        picName = ''.join(picName2)
        with open((img_folder+picName), 'wb') as f:
            f.write(html2.content)
            print('%s已经下载完成...' % picName)
            f.close()


downloadTreads = []                                                 #所有进程的列表

#每一次for循环创建一个线程
for i in range(5500, 5600, 10):                                    #循环10次，创建10个线程（range表示i在5500到5600之间，步频为10）
    downloadTread = threading.Thread(target=getUrl, args=(i,))      #第一个参数是线程函数变量，第二个参数args是一个数组变量参数，如果只传递一个值，就只需要i, 如果需要传递多个参数，那么还可以继续传递下去其他的参数，其中的逗号不能少，少了就不是数组了，就会出错。
    downloadTreads.append(downloadTread)                            #把thread对象追加到列表中
    downloadTread.start()                                           #运行新的线程，先的线程调用geturl方法

#等待所有的线程结束
for downloadTread in downloadTreads:                             #利用for循环，遍历downloadThread列表中的所有thread对象
    downloadTread.join()
print('Done.')


