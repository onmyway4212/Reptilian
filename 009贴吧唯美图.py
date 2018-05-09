import urllib.request
import re
import os


def open_url(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')
    page = urllib.request.urlopen(req)
    html = page.read().decode('utf-8')
    return html


def get_img(html):
    # 正责表达式返回的是图片的网址
    p = r'<img class="BDE_Image".src="([^"]*\.jpg)".*?>'
    imglist = re.findall(p, html)
    try:
        # os.mkdir()用来创建文件夹
        os.mkdir('pic')
    except FileExistsError:
        # 如果文件已经存在则覆盖保存
        pass
    # chdir()用来改变当前工作目录
    os.chdir('pic')
    for each in imglist:
        # 把图片的网址按照/分隔，返回[-1]是列表从右往左数第一个，就是图片名称
        filename = each.split('/')[-1]
        # urlretrieve() 方法直接将远程数据下载到本地
        urllib.request.urlretrieve(each, filename, None)


if __name__ == '__main__':
    url = 'https://tieba.baidu.com/p/3823765471'
    get_img(open_url(url))
    print('下载已完成，文件保存的目录为%s' % os.getcwd())

