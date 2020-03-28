'''
Counter是一个简单的计数器，例如，统计字符出现的个数：
'''

from collections import Counter

c = Counter()

for i in 'Programming':
    c[i] = c[i] + 1

print(c)

c.update('fasfkjsadkl;fjsadlkfjas1')
print(c)
