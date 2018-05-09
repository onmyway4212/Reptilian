import requests
import re
from  bs4 import BeautifulSoup
from selenium import webdriver
import os

if not os.path.exists('d:\\OOXX3\\'):
    os.mkdir('d:\\OOXX3\\')
os.chdir('d:\\OOXX3\\')                                  #改变到当前路径
#url='http://jandan.net/ooxx/page-48#comments'
i = 47
while 0 < i < 100:
    url = 'http://jandan.net/ooxx/page-' + str(i) + '#comments'
    driver = webdriver.PhantomJS(executable_path=r"D:\phantomjs-2.1.1-windows\bin\phantomjs.exe")
    driver.get(url)
    soup=BeautifulSoup(driver.page_source,'html.parser')
    #pages=soup.find_all('li',{'id':re.compile('page-[0-9]+#comments]')})
    pages=soup.find_all('li',{'id':re.compile('comment-[0-9]+')})
    #print(soup)
    for pic in pages:
        n = pic.find("img",{'src':re.compile(r'(.*\.jpg)|(.*\.gif)')})['src']
        name = n.split('/')[-1]
        with open(name,'wb') as f:
            reponse = requests.get(n).content
            f.write(reponse)
            f.close()
            print('%s已下载完成！' % name)
    i-=1

#<img src="http://wx1.sinaimg.cn/mw1024/661eb95cgy1fphv9yqwrig20jk0gke8c.gif" style="max-width: 480px; max-height: 750px;">
#<a href="//wx1.sinaimg.cn/large/7cf5a028gy1fpodp5xhrsg207c0auqv5.gif" target="_blank" class="view_img_link">[查看原图]</a>
#<img src="http://wx1.sinaimg.cn/mw690/7cf5a028gy1fpodp5xhrsg207c0auqv5.gif" style="max-width: 480px; max-height: 750px;">
#<a href="//jandan.net/ooxx/page-48#comments">
#<img src="http://ww1.sinaimg.cn/mw600/61e74233ly1fpmq7xskpgj20m80etn1l.jpg" style="max-width: 480px; max-height: 750px;">