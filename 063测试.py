from selenium import webdriver

brower = webdriver.Firefox()
brower.get('https://www.taobao.com/')
linkElem = brower.find_element_by_link_text('淘抢购')
linkElem.click()


#<h4 class="a-all" id="dg-item-tl-3" data-spm-anchor-id="a21bo.2017.201870.i1.5af911d9FeuJoy">Boden星星装饰卫衣</h4>
#<a target="_blank" href="http://baike.baidu.com/view/1631019.htm">亚历山大·格罗滕迪克</a>
#<a href="https://www.udemy.com/automate/?couponCode=INVENT_WITH_PYTHON">INVENT_WITH_PYTHON</a>
#<a href="https://inventwithscratch.com" class="btn btn-primary">Read Online for Free</a>