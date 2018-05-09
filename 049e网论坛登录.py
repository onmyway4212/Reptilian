import requests

session = requests.Session()

params = {'pwuser':'88186161', 'pwpwd':'18906855486'}
s = requests.post('http://www.e0575.cn/u.php?a=info&uid=1068534', data=params)

print('cookies is set to:')
print(s.cookies.get_dict())

s = session.get('http://www.e0575.cn/apps.php?q=diary&a=detail&did=2867')
print(s.text)
