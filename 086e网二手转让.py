from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
import re

def get_data(i):
    global url1
    list1 = []
    for i in range(1, i+1):
        url1 = 'http://secondhand.e0575.com/'
        url = url1 + '?page=' + str(i)
        html = urlopen(url)
        bsobj = BeautifulSoup(html, 'lxml')
        item = bsobj.find('ul', {'class': 'es_list1_l1'}).findAll('li')
        list1.append(item)
    return list1


def main():
    a =0
    with open("C:/Users/Administrator/Desktop/绍兴二手转让.csv", "w", encoding='utf-8') as f:
        writer = csv.writer(f)
        for t in get_data(3):
            for x in t:
                #f.write("{}\n{}\n\n".format(x.text, url1+x.a['href']))
                writer.writerow([x.text, url1+x.a['href']])
                a+=1
    print('输入%d条数据了！' %a)


if __name__ == "__main__":
    main()
