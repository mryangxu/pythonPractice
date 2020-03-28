import socket, threading, time

# 创建 一个基于IPv4的socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 监听端口
s.bind(('127.0.0.1', 9999))

# 开始监听 参数指定等待连接的最大数量
s.listen(5)
print('Wating for connecting')

def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(10)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connect from %s:%s...' % addr)

# 通过一个永久循环来获取客户端信息
while True:
    # 接收一个新连接
    sock, addr = s.accept()
    # 创建新线程来处理TCP连接
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()





