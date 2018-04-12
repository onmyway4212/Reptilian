from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random
import pymysql

conn = pymysql.connect(host = '127.0.0.1', user = 'root', passwd = 'zh12345', db= 'mysql', charset= 'utf8')
cur = conn.cursor()
cur.execute('use scraping')
random.seed(datetime.datetime.now())

def store(title, content):
    cur.execute("insert into pages (title,content) values (\"%s\",\"%s\")", (title, content))
    cur.connection.commit()


def getlinks(articleurl):
    html = urlopen('https://en.wikipedia.org' + articleurl)
    bsobj = BeautifulSoup(html, 'lxml')
    title = bsobj.find('h1').get_text()
    content = bsobj.find('div', {'id':'mw-content-text'}).find('p').get_text()
    store(title, content)
    return bsobj.find('div', {'id': 'bodyContent'}).findAll('a', href= re.compile('^(/wiki/)((?!:).)*$'))

links = getlinks('/wiki/Kevin_Bacon')
try:
    while len(links) > 0:
        newarticle = links[random.randint(0, len(links)-1)].attrs['href']
        print(newarticle)
        links = getlinks(newarticle)
finally:
    cur.close()
    conn.close()

