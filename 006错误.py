from urllib.request import Request,urlopen
from urllib.error import URLError, HTTPError

req = Request('http://www.962.net/meitu/167729.html')
try:
    response = urlopen(req)
except HTTPError as e:
    print('HTTPError! fulfill the request.')
    print('Error code:', e.code)
    print('Reson:',e.reason)
except URLError as e:
    print('URLError! we failed to reach a sercer')
    print('Error code:', e.code)
    print('Reson:',e.reason)
else:
   print('everything is fine')
