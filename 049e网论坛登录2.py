import requests
from bs4 import BeautifulSoup

url = 'http://www.e0575.cn/read.php?tid=11130880'
#params = {'pwuser':'88186161', 'pwpwd':'18906855486'}
#s = requests.post('http://www.e0575.cn/u.php?a=info&uid=1068534', data=params)

s = requests.get(url).content
bsobj = BeautifulSoup(s, 'lxml')
for a in bsobj.findAll('div', {'class': 'tpc_content'}):
    print(a.get_text())
#<div class="tpc_content">