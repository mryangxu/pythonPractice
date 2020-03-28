'''
如果一个对象没有实现上下文, 我们就不能使用with语句 ,这个时候 可以使用closing()来把这个对象变成上下文对象
'''

from contextlib import closing, contextmanager

from urllib.request import urlopen


with closing(urlopen('https://python.org')) as page:
    for line in page:
        print(line)


# coling也是一个经过@contextmanager 装饰的generator , 这个gennerator编写起来十分简单
@contextmanager
def closing2(thing):
    try:
        yield thing
    finally:
        thing.close()
