# groupby 把迭代器中相邻的重复的元素分组

import itertools

for k, group in itertools.groupby('AAAVVVDDDFGHHHH123222'):
    print(k, list(group))

'''
实际上挑选规则是通过函数来完成的, 只要作用于函数的两个元素返回的值是相等的, 这两个元素就会被分到同一组
'''
for k, g in itertools.groupby('AAAabbbbB', lambda x: x.upper()):
    print(k, list(g))