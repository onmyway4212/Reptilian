from selenium import webdriver

driver = webdriver.PhantomJS(executable_path=r'D:\phantomjs-2.1.1-windows\bin\phantomjs.exe')
driver.get('https://www.baidu.com/')
driver.implicitly_wait(1)
print(driver.get_cookies())