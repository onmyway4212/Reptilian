import requests
from bs4 import BeautifulSoup
import os


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0',
            'Referer': 'http://www.mzitu.com'}
#页面
def pageUrl(i):
    url = 'http://www.shuaia.net/index_'+str(i) + '.html'
    while i < 10:
        i += 1
    wzUrl(url)


#文章链接
def wzUrl(url):
    html = requests.get(url, headers=headers)
    bsobj = BeautifulSoup(html.text, 'lxml')
    for itemUrl in bsobj.findAll('a',{'class':'item-img'}):
        itemUrl2 = itemUrl['href']
        picUrl(itemUrl2)


#图片链接
def picUrl(itemUrl2):
    html = requests.get(itemUrl2, headers=headers)
    bsobj = BeautifulSoup(html.text, 'lxml')
    pUrl= bsobj.findAll('p', {'style': 'text-align: center;'})[0].find('img')
    name = pUrl.split('/')[-1]
    pUrl = 'http://www.shuaia.net'+pUrl['src']
    return name



#保存图片
def save_img(pUrl, name):
    req = requests.get(pUrl, headers=headers)
    name = picUrl()
    if not os.path.exists('D:/pp/'):
        os.mkdir('D:/pp/')
    with open('D:/pp/'+name , 'wb') as f:
        f.write(req.content)

pageUrl(2)