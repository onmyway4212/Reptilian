import requests
import ssl
import json
from bs4 import BeautifulSoup

ssl._create_default_https_context = ssl._create_unverified_context

if __name__ == '__main__':
    headers = {'User-Agent': 'e0575app/3.12.1/403/Android/6.0/PLK-AL10/Wifi',
                'Host': 'client.e0575.com',
                'Connection': 'Keep-Alive',
                'Accept-Encoding': 'gzip'
                }
    url = 'http://client.e0575.com/app.php?a=indexList&c=article&userLoginRequestType=client&userLoginRequestKey=VwVQUgxTUDxRVwdUBVkMBVJVU1QFVwMHBABUWVUFDFRYBgFTXgAFA2tXVFFSUwdXDVEL&authTime=1523240286&iconvAction=toGbk&authType=client&key=664ec8fa7adc31112a7eced2c7cbca2d&authCode=ea3c81e6d00e0cb311621ccca138d01a'
    req = requests.get(url =url, headers=headers).json()
    #print(type(req['value']['list']))
    #title_num = len(req['value']['list'])
    #print('一共有文章%d篇.' % title_num)
    #print(req['value']['list'])
    for each in req['value']['list']:
        try:
            print(each['title'])
        except KeyError:
            pass