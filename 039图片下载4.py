from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup
import os


html = urlopen('http://tieba.baidu.com/p/5537191372')
bsobj = BeautifulSoup(html,'lxml')
images = bsobj.findAll('img',{'class':'BDE_Image'})
img_folder = "D:\\pic\\"
i = 1
for image in images:
    if not os.path.exists(img_folder):
        os.makedirs(img_folder)
    else:
        urls = image['src'].split('/')
        content = urlopen(image['src']).read()
        path = img_folder + urls[-1]
        with open(path, 'wb') as f:
            f.write(content)
            f.close()
            print("%s已下载完成!" % path)
        i+=1