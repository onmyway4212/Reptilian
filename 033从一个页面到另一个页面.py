from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random

random.seed(datetime.datetime.now())
def getlinks(articleurl):
    html = urlopen('https://en.wikipedia.org' + articleurl)
    bsobj = BeautifulSoup(html, 'lxml')
    return bsobj.find('div', {'id': 'bodyContent'}).findAll('a', href= re.compile('^(/wiki/)((?!:).)*$'))

links = getlinks('/wiki/Kevin_Bacon')
while len(links) > 0:
    newarticle = links[random.randint(0, len(links)-1)].attrs['href']
    print(newarticle)
    links = getlinks(newarticle)