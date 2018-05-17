#<img src="http://img.e0575.com/attachment/photo/Day_180515/2720e9e….jpg" onload="loadpic(2)" style="height: 650px; width: 365.625px;">  图片链接
#<a href="http://www.e0575.cn/pai/show.php?mid=2075840500" target="_blank">   主题链接
#<div id="container">
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

url = 'http://www.e0575.cn/pai/'
html = urlopen(url)
bsobj = BeautifulSoup(html, 'lxml')
for title in bsobj.find('div',{'id': 'container'}).findAll('div', {'class': 'tit'}):
    print(title)
