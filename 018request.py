import urllib.request
from urllib.error import URLError, HTTPError

def dirurl():
    d = dir(urllib.request)
    for i in d:
        print(i)
def urlopen():
    url = 'https://www.baidu.com1/search/error.html'
    try:
        s = urllib.request.urlopen(url,timeout = 3)
        s = s.read().decode('utf-8')
    except HTTPError as e:
        print(e)
    else:
        print(s)


if __name__ == '__main__':
    urlopen()

