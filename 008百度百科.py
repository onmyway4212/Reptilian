import urllib.request
import re
from bs4 import BeautifulSoup

def main():
    url = 'https://baike.baidu.com/item/%E5%91%A8%E6%9D%B0%E4%BC%A6#hotspotmining'
    response = urllib.request.urlopen(url)
    html = response.read()
    #bs需要两个参数，第一个是需要提取数据的html,第二个参数是指定解析器
    soup = BeautifulSoup(html, 'html.parser')
    for each in soup.find_all(href = re.compile('item')):
        print(each.text, '->', ''.join(['https://baike.baidu.com',each['href']]))

if __name__ == '__main__':
    main()

