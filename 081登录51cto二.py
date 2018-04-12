import requests
from bs4 import BeautifulSoup

#新建requests会话
s = requests.Session()

#get首页获取csrf值
content=s.get('http://home.51cto.com/home').content
soup = BeautifulSoup(content,"lxml")
token=soup.find('meta',attrs = {'name' : 'csrf-token'})['content']

#构造header和data
headers = {'Host': 'home.51cto.com',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
            'Referer': 'http://home.51cto.com/index?reback=http://www.51cto.com/',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9'
           }

data = {'_csrf':token,
    'LoginForm[username]':'88186161@qq.com',
    'LoginForm[password]':'zh123456',
    'LoginForm[rememberMe]':'0',
    'login-button':'登 录'}

s.post(url='http://home.51cto.com/index',headers=headers,data=data)

result=s.get('http://home.51cto.com/home').text
bsobj = BeautifulSoup(result, 'lxml')
r = bsobj.find('div',{'class':'port_m_box right position_r'}).get_text()
#<div class="port_m_box right position_r">
#print ('恭喜,登陆51cto成功,领取下载豆中..')
print(r)