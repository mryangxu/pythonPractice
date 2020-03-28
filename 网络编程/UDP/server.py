import socket, time

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind(('127.0.0.1', 9999))

print('Bind UDP on 9999...')
while True:
    data, addr = s.recvfrom(1024)
    print('Recvived from %s:%s' % addr)
    time.sleep(1)
    s.sendto(b'Hello %s' % data, addr)

