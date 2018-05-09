import urllib.request
import os


def url_open(url):
    req = urllib.request.Request(url)

    # 添加header伪装成人非爬虫
    req.add_header('User-Agent', 'Mozilla/5.0 \
    (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.65 Safari/537.36')
    response = urllib.request.urlopen(url)
    html = response.read()
    return html


def get_page(url):
    html = url_open(url).decode('uft-8')

    a = html.find('current-comment-page') + 23
    b = html.find(']', a)

    return html[a:b]


def find_imgs(url):
    html = url_open(url).decode('uft-8')
    img_addrs = []

    a = html.find('img src =')
    b = html.find('.jpg', a, a + 255)

    while a != -1:
        b = html.find('.jpg', a, a + 255)
        if b != -1:
            img_addrs.append(html[a + 9:b + 4])
        else:
            b = a + 9

        a = html.find('img src =', b)

    for each in img_addrs:
        print(each)

    return img_addrs


def save_imgs(folder, img_addrs):
    for each in img_addrs:
        filename = each.split('/')[-1]
        with open(filename, wb) as f:
            f.write(img)


# 程序主函数，创建文件夹，保存图片。
def download_mm(folder='ooxx', pages=10):
    # os.mkdir(path)创建单层目录，如果目录存在抛出异常
    # os.chdir(path)改变工作目录
    os.mkdir(folder)
    os.chdir(folder)

    url = 'http://jandan.net/ooxx/'
    pege_num = int(get_page(url))

    for i in range(pages):
        page_num -= i
        page_url = url + 'page' + str(page_num) + '#comments'
        img_addrs = find_imgs(page_url)
        save_imgs(folder, img_addrs)


# __name__ 是当前模块名，当模块被直接运行时模块名为 __main__ 。这句话的意思就是，
# 当模块被直接运行时，以下代码块将被运行，当模块是被导入时，代码块不被运行。
if __name__ == '__main__':
    download_mm()
