import requests
import ssl
import json
from bs4 import BeautifulSoup

ssl._create_default_https_context = ssl._create_unverified_context

if __name__ == '__main__':
    headers = {'android-channel': 'huawei',
                'charset': 'UTF-8',
                'lang': 'zh-cn',
                'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; PLK-AL10 Build/HONORPLK-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/49.0.2623.105 Mobile Safari/537.36 News/146 Android/146 NewsApp/146 SDK/23 VERSION/5.9.5',
                'api-key': 'dongqiudi.com',
                'Host': 'api.dongqiudi.com',
                'Connection': 'Keep-Alive',
                'Accept-Encoding': 'gzip'
                }
    url = 'https://api.dongqiudi.com/app/tabs/android/6.json?after=1523186839&page=2&mark=gif&version=146'
    req = requests.get(url =url, headers=headers).json()

    for each in req['articles']:
        try:
            print(each['title'])
        except KeyError:
            pass
