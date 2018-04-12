from selenium import webdriver

brower = webdriver.Firefox()
brower.get('https://pan.baidu.com/')
linkElem = brower.find_element_by_class_name('pass-link')
linkElem.click()
'''
caunt = brower.find_element_by_id('pwuser')
caunt.send_keys('88186161')
password = brower.find_element_by_id('pwpwd')
password.send_keys('18906855486')
password.submit()
'''
#<p class="tang-pass-footerBarULogin pass-link" title="帐号密码登录" data-type="normal" id="TANGRAM__PSP_4__footerULoginBtn">帐号密码登录</p>