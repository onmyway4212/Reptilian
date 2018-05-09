import requests
from requests.auth import AuthBase
from requests.auth import HTTPBasicAuth

auth = HTTPBasicAuth('不发言我难受', 'shxtl186')
r = requests.post(url= 'https://tieba.baidu.com/index.html',auth = auth)
print(r.text)