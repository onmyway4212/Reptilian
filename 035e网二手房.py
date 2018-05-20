from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
import re

def get_data():
    list1=[]
    global url1
    for i in range(15):
        url1 = 'https://house.e0575.com/'
        url2 = 'list.php?tix=1&odb=gx&page='
        url = url1 + url2 + str(i)
        html = urlopen(url)
        bsobj = BeautifulSoup(html, 'lxml')
        list1.append(bsobj)
    return list1

def main():
    a=0
    with open('C:/Users/Administrator/Desktop/绍兴二手房.csv', 'w', encoding='utf-8') as f:
        for t in get_data():
            for item in t.findAll('div', {'class': 'con1'}):
                for sj in item('p', {'class': 'p3'}):
                    print(item.a.text)
                    print(item.p.get_text())
                    print(item.div.em.get_text())
                    print(sj.text)
                    print(url1 + item.a['href'])
                    f.write("{}, {}, {}, {}\n {}\n\n".format(item.a.text, item.p.get_text(), item.div.em.get_text(), sj.text,
                                                            url1 + item.a['href']))
                    a+=1
    print('一共保存了%d条数据!!!' %a)


if __name__=='__main__':
    main()


