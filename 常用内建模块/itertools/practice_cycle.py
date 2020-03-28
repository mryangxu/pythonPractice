import itertools, time

# cycle 会把一个序列无限的复制下去
cs = itertools.cycle('ABC')

for i in cs:
    print(i)
    time.sleep(1)


'''

会输出
A
B
C
A
B
...

'''