from urllib import request

with request.urlopen('http://cqsq.com/') as f:
    data = f.read()
    print('Status:', f.status, f.reason)
    # for k, v in f.getheaders():
        # print('%s: %s' % (k, v))
    # print('Data:', data.decode('utf-8'))

# 如果我们要实现模拟浏览器发送get请求, 就需要用到request对象, 通过往request对象添加http请求头,就可以把请求伪装城浏览器

req = request.Request('http://cqsq.com/')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
with request.urlopen(req) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    # print('Data:', data.decode('utf-8'))

