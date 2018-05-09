from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC           #webDriverWait 和 EC构成selenium的隐式等待

driver = webdriver.PhantomJS(executable_path=r'D:\phantomjs-2.1.1-windows\bin\phantomjs.exe')
driver.get('http://www.pythonscraping.com/pages/javascript/ajaxDemo.html')

try:
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "loadedButton")))  #By对象表示定位器
finally:
    print(driver.find_element_by_id("content").text)
    driver.close()