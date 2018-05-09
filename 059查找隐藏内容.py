from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement

driver = webdriver.PhantomJS(executable_path=r'D:\phantomjs-2.1.1-windows\bin\phantomjs.exe')
driver.get('http://www.pythonscraping.com/pages/itsatrap.html')
links = driver.find_elements_by_tag_name('a')                                       #找到网页源代码中所有的标签a
for link in links:
    if not link.is_displayed():
        print('the link '+link.get_attribute('href')+' is a trap')

fields = driver.find_elements_by_tag_name('input')                                  #找到网页源代码中所有的标签input
for field in fields:
    if not field.is_displayed():                                                    #通过is_displayed()判断元素在页面上是否可见
        print('Do not change value of '+field.get_attribute('name'))