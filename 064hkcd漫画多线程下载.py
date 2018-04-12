import requests, os, bs4, threading

os.makedirs('d:/xkcd2/', exist_ok=True)

def downloadXkcd(startComic, endComic):
    for urlNumber in range(startComic, endComic):
        if urlNumber == 404:
            return 
        print('Downloading page http://xkcd.com/%s' % (urlNumber))
        res = requests.get('http://xkcd.com/%s' % (urlNumber))
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text, 'lxml')

        comicElem = soup.select('#comic img')
        if comicElem == []:
            print('could not find comic image.')
        else:
            comicUrl = 'http:'+comicElem[0].get('src')
            print('downloading image %s...' % (comicUrl))
            res = requests.get(comicUrl)
            res.raise_for_status()

            imageFile = open(os.path.join('d:/xkcd2', os.path.basename(comicUrl)), 'wb')
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()


downloadTreads = []                                                               #空列表用来存储多个thread对象

#每一次for循环创建一个线程
for i in range(1, 1400, 100):                                                         #1到1400之间，步长为100
    downloadTread = threading.Thread(target=downloadXkcd, args = (i, i+99))      #第一个参数是线程函数变量，第二个参数args是一个数组变量参数，如果只传递一个值，就只需要i, 如果需要传递多个参数，那么还可以继续传递下去其他的参数，其中的逗号不能少，少了就不是数组了，就会出错。
    downloadTreads.append(downloadTread)
    downloadTread.start()

for downloadTread in downloadTreads:
    downloadTread.join()
print('Done.')



'''
构造方法： 
Thread(group=None, target=None, name=None, args=(), kwargs={}) 

　　group: 线程组，目前还没有实现，库引用中提示必须是None； 
　　target: 要执行的方法； 
　　name: 线程名； 
　　args/kwargs: 要传入方法（函数）的参数。

实例方法： 
　　isAlive(): 返回线程是否在运行。正在运行指启动后、终止前。 
　　get/setName(name): 获取/设置线程名。 

　　start():  线程准备就绪，等待CPU调度
　　is/setDaemon(bool): 获取/设置是后台线程（默认前台线程（False））。（在start之前设置）

　　　　如果是后台线程，主线程执行过程中，后台线程也在进行，主线程执行完毕后，后台线程不论成功与否，主线程和后台线程均停止
       　　如果是前台线程，主线程执行过程中，前台线程也在进行，主线程执行完毕后，等待前台线程也执行完成后，程序停止
　　start(): 启动线程。 
　　join([timeout]): 阻塞当前上下文环境的线程，直到调用此方法的线程终止或到达指定的timeout（可选参数）。
'''