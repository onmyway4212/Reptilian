import requests
user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
headers = {'User-Agent': user_agent}
cookies = dict(name='qiye', age = '10')
r = requests.get('https://www.baidu.com/', headers=headers,cookies=cookies)
print(r.cookies.keys())