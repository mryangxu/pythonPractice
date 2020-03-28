'''将上一节的salt改为标准的hmac算法，验证用户口令'''

# -*- coding: utf-8 -*-
import hmac, random

def hmac_md5(key, s):
    return hmac.new(key.encode('utf-8'), s.encode('utf-8'), 'MD5').hexdigest()

class User(object):
    def __init__(self, username, password):
        self.username = username
        self.key = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        self.password = hmac_md5(self.key, password)


db = {
    'micheal': User('micheal', '123456'),
    'bob': User('bob', '123456'),
    'alice': User('alice', '123456')
}

def login(username, password):
    user = db[username]
    return user.password == hmac_md5(user.key, password)

assert login('micheal', '123456')
assert login('bob', '123456')
assert login('alice', '123456')
assert not login('micheal', '123')
assert not login('bob', '123')
assert not login('alice', '123')
print('ok')