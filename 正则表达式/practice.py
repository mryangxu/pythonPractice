import re

rule = r'^\d{3}\-\d{3,8}$'

print(re.match(rule, '010-123456'))

print(re.match(rule, '010 12312'))

# match 方法对字符串进行匹配 匹配成功返回Match对象 失败返回None

# 常见判断方法
str = r'reqeqweq'
if re.match(rule, str):
    print('成功')
else:
    print('未匹配到')


# 正则表达式切分字符串更灵活

print('a b   c'.split(' '))

print(re.split(r'\s+', 'a b  c  d'))

print(re.split(r'[\s\,]+', 'a,b, c  d   , e'))

print(re.split(r'[\s\,\;\d]+', 'a234b,c;d;  e;;;;f'))

# 如果正则表达式中定义了分组 就可以在结果中使用group提取出来
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-123')
print(m)
print(m.group(0))
print(m.group(1))
print(m.group(2))
# print(m.group(3)) # 超出会报IndexError

# 注意 group(0) 永远是原始字符串 1 2 分别是子串 提取子串非常有帮助



# 当我们在使用正则表达式时，re内部模块会干两件事：
    # 1.编译正则表达式，如果正则表达式的字符串本身不合法会报错
    # 2.用编译后的正则表达式去匹配字符串
# 如果一个正则表达式要使用几千次，出于效率考虑，应该先预编译正则表达式，接下来重复使用的时候就不需要预编译这个步骤了

# 编译
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
# 使用
print(re_telephone.match('010-12345678').groups())
# 编译后直接生成了Regular Expression对象，由于该对象已经包含了正正则表达式，所以调用对应的方法不用给出正则表达式字符串

