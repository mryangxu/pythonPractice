'''
namedtuple 是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，
并可用属性而不是索引来引用tuple中的元素
'''

from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
assert p.x==1, p.x
assert isinstance(p, Point), p
assert isinstance(p, tuple), p

'''
使用list存储数据时，按索引访问元素很快，但是插入和删除就很慢了，因为list是线性存储，
当数据量很大的时候，插入和删除的效率很低;
deque为了高效实现插入和删除的双向列表，适用于队列和栈
'''
from collections import deque
q = deque(['a', 'b', 'c', 'd'])
q.append('x')
q.appendleft('y')
print(q)
q.pop()
q.popleft()
print(q)

print('')
'''
使用dict的时候，如果key不存在就会抛出KeyError异常。如果希望key不存在的时，返回一个默认值，就使用defaultdict
'''
from collections import defaultdict
dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'x'
assert dd['key1'] == 'x', dd['key1']
assert dd['key2'] == 'N/A', dd['key2']

'''
使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。
如果要保持Key的顺序，可以用OrderedDict(按照插入的顺序)
'''
from collections import OrderedDict
d = dict([('a', 1), ('b', 2), ('c', 3)])
d1 = OrderedDict(a=1, b=2, c=3)
print(d)
print(d1)

print()
print('OrderedDict 实现一个先进先出的dict')

class LastUpdatedOrderedDict(OrderedDict):

    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0 # 判断是否包含
        if len(self) - containsKey >= self._capacity: # 字典已经装满且不包含 说明是新增
            # 移除第一个进入的元素
            last = self.popitem(last=False)
            print('remove:', last)
        if containsKey: # 包含 说明是修改
            del self[key] # 删除之前的元素
            print('set', (key, value))
        else: # 新增
            print('add', (key, value))

        # 用OrderDict执行新增操作
        OrderedDict.__setitem__(self, key, value)

dl =LastUpdatedOrderedDict(2)

dl['x'] = 123
dl['y'] = 123
dl['z'] = 12
dl['a'] = 12

print(dl)