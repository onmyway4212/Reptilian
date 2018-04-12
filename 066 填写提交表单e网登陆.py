from selenium import webdriver

brower = webdriver.Firefox()
brower.get('http://www.e0575.cn/login.php')
caunt = brower.find_element_by_id('pwuser')
caunt.send_keys('88186161')
password = brower.find_element_by_id('pwpwd')
password.send_keys('18906855486')
password.submit()