import requests
url = 'https://www.jd.com/'
r = requests.get(url).text
print(len(r))
with open('jd.html','w',encoding='utf-8') as f:
    f.write(r)