from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
import re

i = 1


with open('C:/Users/Administrator/Desktop/绍兴e网招聘.csv','w',encoding='utf-8') as f:

    while i < 10:
        url = 'https://job.e0575.com/list.php?tIx=40' + '&page=' + str(i)
        html = urlopen(url)
        bsobj = BeautifulSoup(html, 'lxml')


        for item in bsobj.findAll('li', {'class': 'bg1'}):
            #print(item)
            #print('---', item.span.text, '-----', item.div.text, '-----', item.a['title'], '\n', '-----',item.a['href'])
            for gz in item('div',{'class': 'dd1'}):
                for sj in item('div',{'class': 'dd2'}):
                    f.write("{}, {}, {}, {}, {}\n{}\n\n".format(item.span.text, item.div.text, item.a['title'], gz.text, sj.text,item.a['href']))
                    #print('---', item.span.text, '---', item.div.text, '---', item.a['title'], '---',gz.text,'---', sj.text,'---''\n', item.a['href'],'\n')
        i+=1


f.close()

