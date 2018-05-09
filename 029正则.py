from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bsobj = BeautifulSoup(html, 'xml')
images = bsobj.findAll('img', {'src': re.compile(r"\.\./img/gifts/img.*\.jpg")})
for image in images:
    print(image['src'])
