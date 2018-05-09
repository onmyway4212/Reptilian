import requests
from bs4 import BeautifulSoup

#session = requests.Session()
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
           'accept': 'image / webp, image / apng, image / *, * / *;q = 0.8'}
url = 'https://www.whatismybrowser.com/detect/what-http-headers-is-my-browser-sending'
req = requests.get(url, headers=headers)
bsobj = BeautifulSoup(req.text, 'lxml')                                                #bs4解析的是requests的req.text
print(bsobj.find('table',{'class':'table table-striped'}).get_text())