import time, threading

# 假定这是你的银行存款数
balance=0
def change_it(n):
    # 先存后取 结果应该为0
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(100000): # 当操作次数变多后就会出现数据污染
        change_it(i)

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))

t1.start()
t2.start()
t1.join()
t2.join()
print(balance)


# 采用锁机制 解决上面数据污染问题
balance = 0
lock = threading.Lock()

def run_thrad2(n):
    for i in range(100000):
        # 先获取锁
        lock.acquire()
        try:
            # 放心的改吧
            change_it(i)
        finally:
            # 改完后一定要释放锁 不然其它进程没办法操作 苦苦的等
            lock.release()


t3 = threading.Thread(target=run_thrad2, args=(3,))
t4 = threading.Thread(target=run_thrad2, args=(4,))

t3.start()
t4.start()
t3.join()
t4.join()
print('balance is %d' % balance)
