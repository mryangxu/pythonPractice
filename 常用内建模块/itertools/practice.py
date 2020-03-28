'''python 内建模块 itertools提供了非常有用的处理迭代的函数'''
import itertools
import time

# count会创建一个无线迭代器
natuals = itertools.count(1)
for i in natuals:
    print(i)
    time.sleep(1)

'''

输出结果
1
2
3
4
5
...

'''