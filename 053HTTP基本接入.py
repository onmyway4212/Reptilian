import requests
from requests.auth import AuthBase
from requests.auth import HTTPBasicAuth

auth = HTTPBasicAuth('zhanghao', 'password')
r = requests.post(url= 'http://www.pythonscraping.com/pages/auth/login.php',auth = auth)
print(r.text)