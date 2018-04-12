from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('http://www.e0575.com/')
bsobj = BeautifulSoup(html, 'xml')
for each in bsobj.findAll('ul', {'class':'ts_t2'}):
    each = each

    print(each)