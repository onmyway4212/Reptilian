from selenium import webdriver

brower = webdriver.Firefox()
brower.get('https://www.taobao.com/')
try:
    elem = brower.find_element_by_class_name('goods-hd mod-hd com-hd')
    print('找到了这个的标签名字%s!' %(elem.tag_name))
except:
    print('找不到这个名字！')

#<h3 class="goods-hd mod-hd com-hd">…</h3>
#<div class="layer">
#<li class="nav-item dropdown">…</li>