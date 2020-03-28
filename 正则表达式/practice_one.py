'''
请尝试写一个验证Email地址的正则表达式。版本一应该可以验证出类似的Email：

someone@gmail.com
bill.gates@microsoft.com
'''
import re

def is_valid_email(addr):
    if re.match(r'\w+\.?\w+@\w+.com$', addr):
        return True
    else:
        return False

# 测试:
assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')

'''
版本二可以提取出带名字的Email地址：

<Tom Paris> tom@voyager.org => Tom Paris
bob@example.com => bob
'''
def name_of_email(add):
    m = re.match(r'^\<?([\w\s]+)\>?[\w\s@\.]+', add)
    return m.group(1)

# 测试:
assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')
