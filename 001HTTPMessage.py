import urllib
import urllib.request

def print_list(list):
    for i in list:
        print(i)

def demo():
    s = urllib.request.urlopen('http://blog.csdn.net')
    #info()返回HTTPMessage实例
    msg = s.info()
    #dir函数可以查看该方法所有的函数
    #print_list(dir(msg))
    #print_list(msg.items())
    head = msg._headers
    print_list(head)

if __name__ =='__main__':
    demo()