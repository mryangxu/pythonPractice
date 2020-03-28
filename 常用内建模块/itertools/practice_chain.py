# chain可以把一组迭代对象串联起来,形成一个更大的迭代对象
import itertools
for c in itertools.chain('ABC', '!@#', '123'):
    print(c)