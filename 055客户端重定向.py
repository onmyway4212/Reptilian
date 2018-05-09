from selenium import webdriver
import time
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import StaleElementReferenceException

def waitForLoad(driver):
    elem = driver.find_element_by_tag_name("html")
    count = 0
    while True:
        count +=1
        if count >20:
            print('timing out of after 10 second and returning')
            return
        time.sleep(0.5)
        try:
            elem == driver.find_element_by_tag_name("html")      #每0.5秒检查一次网页，看看html标签还在不在
        except StaleElementReferenceException:
            return


driver = webdriver.PhantomJS(executable_path=r'D:\phantomjs-2.1.1-windows\bin\phantomjs.exe')
driver.get('http://www.pythonscraping.com/pages/javascript/redirectDemo2.html')
waitForLoad(driver)
print(driver.page_source)
