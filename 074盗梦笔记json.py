import requests
import json
from bs4 import BeautifulSoup

user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
headers = {'User-Agent': user_agent}
r = requests.get('http://www.seputu.com/',  headers=headers)
bsobj = BeautifulSoup(r.text, 'html.parser')
content = []

for mulu in bsobj.find_all(class_='mulu'):
    h2 = mulu.find('h2')
    if h2!=None:
        h2_title = h2.string
        list = []
        print(h2_title)
        for a in mulu.find(class_='box').find_all('a'):
            href = a['href']
            box_title = a.get('title')
            list.append({'href':href, 'box_title':box_title})
        content.append({'title':h2_title, 'content':list})
with open('qiye.json', 'w') as fp:
    json.dump(content, fp=fp, indent=4)            #按indent的数量显示前面的空白