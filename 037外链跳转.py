from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re
import datetime
import random

pages = set()  #创建一个pages集合
random.seed(datetime.datetime.now())   #datetime.datetime.now()是现在时间。用当前时间作为种子产生不同的随机数

#获取页面所有内链的列表品
def getinternallinks(bsobj, includeurl):
    includeurl = urlparse(includeurl).scheme + '://'+urlparse(includeurl).netloc
    #ParseResult(scheme='http', netloc='www.cwi.nl:80', path='/%7Eguido/Python.html',params='', query='', fragment='')
    internallinks = []
    #找出以/开头的链接
    for link in bsobj.findAll('a', href = re.compile('^(/|.*'+includeurl+')')):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internallinks:
                if(link.attrs['href'].startswitch('/')):              #startswith() 方法用于检查字符串是否是以指定子字符串开头，如果是则返回 True，否则返回 False
                    internallinks.append(includeurl+link.attrs['href'])
                else:
                    internallinks.append(link.attrs['href'])
    return internallinks

#获取页面所有外链的列表
def getexternallinks(bsobj, excluderurl):
    externallinks = []
    #找出所有http或www开头且不包含当前url的链接
    for link in bsobj.findAll('a', href=re.compile("^(http|www)((?!"+excluderurl+").)*$")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externallinks:
                externallinks.append(link.attrs['href'])
    return externallinks

def splitaddress(address):
    addressparts = address.replace('http://', '').spilt('/')  #Python replace() 方法把字符串中的 old（旧字符串） 替换成 new(新字符串)
    return addressparts


def getradnomexternallink(startingpages):
    html = urlopen(startingpages)
    bsobj = BeautifulSoup(html, 'lxml')
    externallinks = getexternallinks(bsobj, urlparse(startingpages).netloc)
    if len(externallinks) == 0:
        print('no external links, looking around the site for one')
        domain = urlparse(startingpages).scheme + '://'+ urlparse(startingpages).netloc
        internallinks = getexternallinks(bsobj, domain)
        return getradnomexternallink(internallinks[random.randint(0, len(internallinks)-1)])
    else:
        return externallinks[random.randint(0, len(externallinks)-1)]


def followexternalonly(startingsite):
    externallink = getradnomexternallink(startingsite)
    print('随机外链是:'+externallink)
    followexternalonly(externallink)


followexternalonly('http://www.shaoxing.com.cn/')

