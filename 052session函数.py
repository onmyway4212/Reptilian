import requests

#会话(session)对象会持续跟踪会话信息，像cookies、header，甚至包括HTTP协议的信息
session = requests.session()

params = {'username':'zhanghao', 'password':'password'}
s = session.post('http://www.pythonscraping.com/pages/cookies/welcome.php', params)
print('cookie is set to:')
print(s.cookies.get_dict())                   #打印cookies信息的字典
print('------------------------------------')
print('going to profile page...')
s = session.get('http://www.pythonscraping.com/pages/cookies/profile.php')
print(s.text)