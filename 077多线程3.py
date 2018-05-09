import time, threading

# 假定这是你的银行存款:
balance = 0


def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n


def run_thread(n):
    for i in range(100000):
        change_it(n)


t1 = threading.Thread(target=run_thread, args=(5,))     #在封闭的右括号左边加一个逗号，加上逗号才是元组，才会将字符串"muise"作为一个参数传递，否则字符串的每个字符都会作为一个单独的参数传递
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)


'''
  我们定义了一个共享变量balance，初始值为0，并且启动两个线程，先存后取，理论上结果应该为0，
  但是，由于线程的调度是由操作系统决定的，当t1、t2交替执行时，只要循环次数足够多，balance的
  结果就不一定是0了。
  
   如果我们要确保balance计算正确，就要给change_it()上一把锁，当某个线程开始执行change_it()时，
   我们说，该线程因为获得了锁，因此其他线程不能同时执行change_it()，只能等待，直到锁被释放后，
   获得该锁以后才能改。
'''