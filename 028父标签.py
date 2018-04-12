from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bsobj = BeautifulSoup(html, 'xml')
print(bsobj.find('img', {'src': '../img/gifts/img1.jpg'}).parent.previous_sibling.get_text())            #previous_sibling 前一个兄弟标签