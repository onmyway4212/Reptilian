import requests


params = {'username':'zhanghao', 'password':'password'}
r = requests.post('http://www.pythonscraping.com/pages/cookies/welcome.php', params)  #向欢迎页面发送一个登录参数
print('cookie is set to:')
print(r.cookies.get_dict())                   #打印cookies信息的字典
print('------------------------------------')
print('going to profile page...')

r = requests.get('http://www.pythonscraping.com/pages/cookies/profile.php', cookies = r.cookies)   #返回的结果r的类型<class 'requests.models.Response'>
print(r.text)