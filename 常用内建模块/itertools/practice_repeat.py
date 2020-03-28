# repeat 会把一个元素无限复制下去 , 第二个参数可以限定重复次数

import itertools

ls = itertools.repeat('123', 4)
for i in ls:
    print(i)

'''

输出
123
123
123
123

'''