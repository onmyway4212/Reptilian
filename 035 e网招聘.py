from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
import re


def get_data():
    list1 = []
    for i in range(1, 10):
        url = 'https://job.e0575.com/list.php?tIx=40' + '&page=' + str(i)
        html = urlopen(url)
        bsobj = BeautifulSoup(html, 'lxml')
        list1.append(bsobj)
    return list1


def main():
    i=0
    with open('C:/Users/Administrator/Desktop/绍兴e网招聘.csv', 'w', encoding='utf-8') as f:
        for a in get_data():
            for item in a.findAll('li', {'class': 'bg1'}):
                for gz in item('div', {'class': 'dd1'}):
                    for sj in item('div', {'class': 'dd2'}):
                        f.write("{}, {}, {}, {}, {}\n{}\n\n".format(item.span.text, item.div.text, item.a['title'], gz.text,
                                                                    sj.text, item.a['href']))
                        i+=1
    print('保存了%d条数据！' %i)


if __name__=='__main__':
    main()
