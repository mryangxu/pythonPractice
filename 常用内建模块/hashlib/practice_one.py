# 根据用户输入的口令，计算出存储在数据库中的MD5口令：
import hashlib
def calc_md5(s):
    md5 = hashlib.md5()
    md5.update(s.encode('utf-8'))
    return md5.hexdigest()

print(calc_md5('123'))

