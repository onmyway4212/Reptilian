from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
browser = webdriver.Firefox()
browser.get('https://www.jd.com/')
htmlElem = browser.find_element_by_tag_name('html')
htmlElem.send_keys(Keys.END)    #滚动到页面底部
time.sleep(3)
htmlElem.send_keys(Keys.HOME)   #滚动到页面顶部
time.sleep(2)
browser.quit()                  #关闭浏览器