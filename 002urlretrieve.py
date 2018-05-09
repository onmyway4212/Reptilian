import urllib
import urllib.request

def print_list(list):
    for i in list:
        print(i)

def demo():
    s = urllib.request.urlopen('http://blog.csdn.net')
    msg = s.info()
    #dir函数可以查看该方法所有的函数
    #print_list(dir(msg))
    #print_list(msg.items())
    print(print_list(msg._headers))




def progress(blk,blk_size,totalsize):

    print(blk,blk_size,totalsize)
    #print('%d/%d -%.02f%%' % (blk*blk_size,total_size,(float)(blk *blk_size)*100/total_size))

def retrieve():
    urllib.request.urlretrieve('http://blog.csdn.net','index.html',reporthook = progress)


if __name__ =='__main__':
    retrieve()