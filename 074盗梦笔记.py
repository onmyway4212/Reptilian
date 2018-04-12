import requests
from bs4 import BeautifulSoup
import re

url = 'http://www.seputu.com/'
req = requests.get(url).content
bsobj = BeautifulSoup(req, 'lxml')

with open('C:/Users/Administrator/Desktop/盗梦笔记.csv', 'w', encoding='utf-8') as f:
    for title in bsobj.findAll('a', href=re.compile(r'http://seputu.com/biji.+?\.html')):
        print(title.get_text())
        print(title['href'])
        f.write("{}\n {}\n\n".format(title.get_text(),title['href']))

f.close()


#href = "http://seputu.com/biji2/76.html"
