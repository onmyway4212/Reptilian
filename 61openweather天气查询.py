from selenium import webdriver
from bs4 import BeautifulSoup
import re


drive = webdriver.PhantomJS(executable_path=r'D:\phantomjs-2.1.1-windows\bin\phantomjs.exe')
city = input("请输入您要查询天气的城市名称:").lower()
drive.get(r'http://openweathermap.org/find?q={0}'.format(city))
content = drive.page_source.lower()
matchResult = re.search(r'<a href="(.+?)">\s+'+city+'.+?]', content)
temp = matchResult.group(0)
bsobj = BeautifulSoup(temp, 'lxml')

if bsobj.get_text():
    print(bsobj.get_text())
else:
    print('查不到，请检查城市名字')