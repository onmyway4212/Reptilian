import urllib.request

#urlopen返回一个类文件，可用用read()方式读取内容
#geturl()返回请求的url
#getcode()返回http状态码
url = 'http://n1.itc.cn/img8/wb/recom/2016/09/01/147267775385109864.JPEG'
response = urllib.request.urlopen(url)
tu = response.read()

#‘w’以写入的方式打开文件  'b'以二进制的方式打开文件
with open('tu.jpg','wb') as f:
    f.write(tu)
