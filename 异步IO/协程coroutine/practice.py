# 消费者
def consumer():
    r = ''
    while True:
        n = yield r
        print('n---', n)
        print('r---', r)
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'

# 生产者
def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n += 1
        print('[PRODUCE] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCE] Producing return: %s' % r)
    c.close()

c = consumer()
produce(c)