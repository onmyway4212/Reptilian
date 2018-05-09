from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random

#random.seed(datetime.datetime.now())
def getlinks(articleurl):
    html = urlopen('https://baike.baidu.com' + articleurl)
    bsobj = BeautifulSoup(html, 'lxml')
    return bsobj.find('div', {'class': 'content-wrapper'}).findAll('a', href= re.compile('^(/item/)((?!:).)*$'))

links = getlinks('/item/%E7%8C%AA%E5%85%AB%E6%88%92/769')   #links返回页面所有网址的bs对象
while len(links) > 0:
    newarticle = links[random.randint(0, len(links)-1)].attrs['href']    #random.randint(0, len(links)-1)返回0到len(links)-1之间的一个随机数
    print('https://baike.baidu.com'+newarticle)
    links = getlinks(newarticle)                                        #newarticle是随机生成的新链接

