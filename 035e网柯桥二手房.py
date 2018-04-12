from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
import re

i = 1


with open('C:/Users/Administrator/Desktop/柯桥二手房.csv','w',encoding='utf-8') as f:

    while i < 15:
        url1 = 'https://kqfc.e0575.com/'
        url2 = 'list.php?tix=1&page='
        url = url1 + url2 + str(i)
        html = urlopen(url)
        bsobj = BeautifulSoup(html, 'lxml')

        for item in bsobj.findAll('div', {'class': 'con1'}):
            for sj in item('p', {'class': 'p3'}):
                print(item.a.text)
                print(item.p.get_text())
                print(item.div.em.get_text())
                print(sj.text)
                print(url1 + item.a['href'])
                f.write("{}, {}, {}, {}\n {}\n\n".format(item.a.text, item.p.get_text(), item.div.em.get_text(), sj.text, url1+item.a['href']))

        i+=1

f.close()
# https://kqfc.e0575.com/show.php?nId=7354426
# https://kqfc.e0575.com/list.php?tix=1&page=2