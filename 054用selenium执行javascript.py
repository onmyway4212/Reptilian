from selenium import webdriver
from bs4 import BeautifulSoup
import time

drive = webdriver.PhantomJS(executable_path=r'D:\phantomjs-2.1.1-windows\bin\phantomjs.exe')
drive.get('http://www.pythonscraping.com/pages/javascript/ajaxDemo.html')
time.sleep(3)

print(drive.find_element_by_id('content').text)      #用定位器表示:  driver.find_element(By.ID, "content").text
drive.close()