# 通过takewhile()可以根据条件判断截取一个有限的序列

import itertools

x = itertools.count(1)

y = itertools.takewhile(lambda x: x <= 10, x)

print(list(y))