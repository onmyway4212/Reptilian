import requests, os, bs4

url = 'http://xkcd.com'
os.makedirs('d:/xkcd', exist_ok=True)
while not url.endswith('#'):

    #download the page
    print('downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()                             #如果下载文件出错，这将抛出异常。确保程序在下载失败时停止

    soup = bs4.BeautifulSoup(res.text, 'lxml')

    #find the url of the comic image.
    comicElem = soup.select('#comic img')              #带有id属性为comic img的元素
    if comicElem == []:
        print('could not find comic image.')
    else:
        comicUrl = 'http:' + comicElem[0].get('src')
        # download the image.
        print('downloading image %s...' % (comicUrl))
        res = requests.get(comicUrl)
        res.raise_for_status()

        #save the image to ./xkcd.
        imageFile = open(os.path.join('d:/xkcd', os.path.basename(comicUrl)), 'wb')          #os.path.basename(path)返回path最后的名字，path以/或\结尾，则返回空
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

    #get the prev button's url.
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prevLink.get('href')

print('Done.')

'''
soup.select('div')                        所有名为<div>的元素
soup.select('#author')                    带有id属性为author的元素
soup.select('.notice')                    所有使用CSS class属性名为notice的元素
soup.select('div span')                   所有在<div>元素之内的<span>元素
soup.select('div > span')                 所有直接在<div>元素之内的<span>元素，中间没有其他元素
soup.select('input[name]')                所有名为<input>，并且有个name属性，其值无所谓的元素
soup.select('input[type="button"]')       所有名为<input>,并有一个type属性，其值为button的元素
'''