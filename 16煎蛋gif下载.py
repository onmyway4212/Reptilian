import requests
import re
from bs4 import BeautifulSoup
from selenium import webdriver
import os
import threading
import time


if not os.path.exists('d:\\OOXX2\\'):
    os.mkdir('d:\\OOXX2\\')
os.chdir('d:\\OOXX2\\')                                  #改变到当前路径
#url='http://jandan.net/ooxx/page-48#comments'

def main(i):
    url = 'http://jandan.net/ooxx/page-' + str(i) + '#comments'
    driver = webdriver.PhantomJS(executable_path=r"D:\phantomjs-2.1.1-windows\bin\phantomjs.exe")
    driver.get(url)
    soup=BeautifulSoup(driver.page_source,'html.parser')
    #pages=soup.find_all('li',{'id':re.compile('page-[0-9]+#comments]')})
    pages=soup.find_all('p', {'style': 'position: relative;'})
    #print(soup)
    for pic in pages:
        n = pic.findAll("a", {'href': re.compile(r'//w.+?\.gif')})
        for n1 in n:
            n1 = n1['href']
            n1 = 'http:' + n1
            name = n1.split('/')[-1]
            with open(name,'wb') as f:
                reponse = requests.get(n1).content
                f.write(reponse)
                f.close()
                print('%s已下载完成！' % name)
                time.sleep(1)



downloadTreads = []

#每一次for循环创建一个线程
for i in range(1, 87):
    downloadTread = threading.Thread(target=main, args=(i,))      #第一个参数是线程函数变量，第二个参数args是一个数组变量参数，如果只传递一个值，就只需要i, 如果需要传递多个参数，那么还可以继续传递下去其他的参数，其中的逗号不能少，少了就不是数组了，就会出错。
    downloadTreads.append(downloadTread)
    downloadTread.start()

for downloadTread in downloadTreads:
    downloadTread.join()
print('Done.')