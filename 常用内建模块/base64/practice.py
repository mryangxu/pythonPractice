'''
请写一个能处理去掉=的base64解码函数：
'''
import base64

def safe_base64_decode(s):

    # 获取4的余数
    remainder = len(s) % 4

    temp_str = ''
    if remainder:
        # 组装等号
        for i in range(remainder):
            temp_str += '='

    # 拼接临时字串
    s += temp_str.encode('utf-8') # 转为bytes
    # 使用自带解码函数
    print(base64.urlsafe_b64decode(s))



# 测试:
safe_base64_decode(b'YWJjZA==')
safe_base64_decode(b'YWJjZA')
# assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
# assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('ok')