import threading, multiprocessing
print(multiprocessing.cpu_count())

# 死循环方法
def loop():
    x = 0
    while True:
        x  = x ^ 1
        print(x)


for i in range(multiprocessing.cpu_count()):
    t = threading.Thread(target=loop)
    t.start()

'''python的线程虽然是真的线程， 但是在python解释器中有一个GIL锁（Global Interpreter Lock）任何python执行前 必须先获得GIL锁，
然后每执行100条字节码，解释器就会自动释放GIL锁，让其它线程有机会执行。这个GIL全局锁实际上把所有线程要执行的代码都上了锁，所以，
多线程在Python中只能交替执行，即使100个线程跑在100核的CPU上一只能使用到1个核'''