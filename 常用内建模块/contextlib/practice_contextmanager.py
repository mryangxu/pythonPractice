'''
编写__enter__和__exit__比较繁琐 ,python的标准库 contextlib 提供了更简单的写法
'''

from contextlib import contextmanager

class Query(object):
    def __init__(self, name):
        self.name = name

    def query(self):
        print('query info about %s...' % self.name)

@contextmanager
def create_query(name):
    print('Begin')
    q = Query(name)
    yield q
    print('End')

with create_query('x') as q:
    q.query()


# 很多时候我们希望在代码的前后自动执行特定代码 也可以使用contextmanager
@contextmanager
def tag(name):
    print('<%s>' % name)
    yield
    print('</%s>' % name)


with tag('h1'):
    print('hello')
    print('world!')