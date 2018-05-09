import urllib.request
import urllib.parse  # parse解析
import json
import time

while True:
    content = input('请输入需要翻译的内容:(q退出)')
    if content == 'q' or content == 'Q':
        break
    if content == '':
        continue

    # url是head->general->request url 的地址
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'

    # data字典的内容从网页源码的formdata中复制过来,i后面是翻译前的，这边是content
    # 字典中很多项都不是必须的
    data = {
        'i': content,
        'from': 'AUTO',
        # 'to':'AUTO',
        # 'smartresult':'dict',
        # 'client':'fanyideskweb',
        # 'salt':'1516274142822',
        # 'sign':'d29f2353c8b2be79f020695478a3863d',
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        # 'action':'FY_BY_REALTIME',
        'typoResult': 'flase'
    }

    # encode(utf-8)编码成utf8格式,decode('utf-8')是把其他编码形式变成unicode编码形式
    # urllib.parse.urlencode()把字符串转换为 application/x-www-form-urle格式
    data = urllib.parse.urlencode(data).encode('utf-8')

    # 修改user-agent
    req = urllib.request.Request(url, data)
    req.add_header('Referer', 'http://fanyi.youdao.com/')
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')

    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')

    # json.loads()把html变成一个字典
    target = json.loads(html)
    print('翻译结果: %s' % (target['translateResult'][0][0]['tgt']))
    print('------------------------------------------------------------------------------')
    print('原html的打印结果是:\n %s' % html)
    print('------------------------------------------------------------------------------')
    print('user-agent 的内容是：\n %s' % req.headers)
    print('\n')

    # 延迟提交数据,这边是休息2秒。避免同一ip在短时间内进行访问
    time.sleep(2)
