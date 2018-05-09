import requests
proxies = {'http':'222.183.214.104:8123',
            'http':'115.223.205.116:9000',
            'http':'117.90.0.54:9000',
           'http':'101.4.136.34:81'
            }
r = requests.get('http://github.com/', timeout=10, proxies=proxies)
print(r.url)
print(r.status_code)
print(r.history)