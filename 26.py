from selenium import webdriver
import  matplotlib
import time

def scroll(n,i):
    return "window.scrollTo(0,(document.body.scrollHeight/{0})*{1});".format(n,i)

url = 'https://www.jd.com/'
firefox = webdriver.Firefox()
firefox.maximize_window()
firefox.get(url)

n = 10
for i in range(0,n+1):
    s = scroll(n,i)
    print(s)
    firefox.execute_script(s)
    time.sleep(1)

print(len(firefox.page_source))
with open("jd2.html",'w',encoding="utf-8",errors='ignore') as f:
    f.write(firefox.page_source)