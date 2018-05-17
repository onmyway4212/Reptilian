from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
import re

with open('C:/Users/Administrator/Desktop/绍兴二手转让.csv','w',encoding='utf-8') as f:
    a=0
    for i in range(1,5):
        url1 = 'http://secondhand.e0575.com/'
        url = url1 + '?page=' + str(i)
        html = urlopen(url)
        bsobj = BeautifulSoup(html, 'lxml')
        for t in bsobj.find('ul',{'class': 'es_list1_l1'}).findAll('li'):
            f.write( "{}\n{}\n\n".format(t.text, url1+t.a['href']))
            '''
            print(t.text)
            print(url1+t.a['href'])
            print('--------------------------------------------------------------------------')
            '''
            a+=1
    print('一共有%d条信息被打印！' %a)

'''
def get_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    soup = soup.find('div', {'id': 'listZone'}).findAll('a')
    return soup


def main():
    with open("hello.tsv", "w") as fh:
        fh.write("url\ttitile\n")
        for item in get_data(URL + "/gdyw.htm"):
            fh.write("{}\t{}\n".format(URL + item.get("href"), item.get_text()))


if __name__ == "__main__":
    main()
'''