'''
只要实现了上下文管理 就可以使用with语句

实现上下文管理是通过__enter__和__exit__这两个方法实现的, 例如, 下面这个class实现了这两个方法
'''

class Query(object):
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print('Begin')
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print('Error')
        else:
            print('End')

    def query(self):
        print('Query info about %s...' % self.name)

with Query('bob') as q:
    q.query()
