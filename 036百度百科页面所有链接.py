from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

def main():
    url = 'https://baike.baidu.com/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB'
    html = urlopen(url)
    bsobj = BeautifulSoup(html, 'lxml')

    for each in bsobj.findAll('a', href = re.compile('^/item/.+')):
        print(each.text, '->', ''.join(['https://baike.baidu.com', each['href']]))

if __name__ == '__main__':
    main()
