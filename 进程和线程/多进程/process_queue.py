'''进程间的通信'''
from multiprocessing import Process, Queue
import os, time, random

# 定义写子进程
def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())

# 第一读子进程
def read(q):
    print('Process to read: %s' % os.getpid())
    while(True):
        value = q.get()
        print('Get %s to quequ...' % value)


if __name__ == '__main__':
    # 父进程创建Queue 然后传递给各个子进程
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))

    # 启动读子进程
    pw.start()

    # 启动写子进程
    pr.start()

    # 等待写紧张执行完毕
    pw.join()

    # 读子进程是死循环 手动结束
    pw.terminate()
