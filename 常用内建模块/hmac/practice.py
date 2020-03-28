import hmac

message = 'Hello, '
key = 'secret'
h = hmac.new(key.encode('utf-8'), message.encode('utf-8'), digestmod='MD5')
h.update('world!'.encode('utf-8'))
print(h.hexdigest())