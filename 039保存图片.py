from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/')
bsobj = BeautifulSoup(html,'lxml')
image1 = bsobj.find('a',{'id':'logo'}).find('img')['src']
urlretrieve(image1,'1.jpg')