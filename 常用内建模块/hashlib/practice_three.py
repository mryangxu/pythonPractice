'''
根据用户输入的登录名和口令模拟用户注册，计算更安全的MD5：
'''

import hashlib, random

db = {}

def register(username, password):
    db[username] = get_md5(password + 'test_salt')


def get_md5(s, p):
    return hashlib.md5((s+p).encode('utf-8')).hexdigest()

class User(object):
    def __init__(self, username, password):
        self.username = username
        self.salt = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        self.password = get_md5(self.salt, password)

db = {
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
}
def login(username, password):
    user = db[username]
    return user.password == get_md5(user.salt, password)

# 测试:
assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')