'''远程开机'''

import struct
import socket
import time
from http.client import HTTPResponse


def wake_up(mac='DC-4A-3E-78-3E-0A'):
    MAC = mac
    # print(MAC)
    # raise Exception('exit')
    # 192.168.0.255
    BROADCAST = "192.168.1.55"
    if len(MAC) != 17:
        raise ValueError("MAC address should be set as form 'XX-XX-XX-XX-XX-XX'")
    mac_address = MAC.replace("-", '')
    data = ''.join(['FFFFFFFFFFFF', mac_address * 20])  # 构造原始数据格式
    send_data = b''

    # 把原始数据转换为16进制字节数组，
    for i in range(0, len(data), 2):
        send_data = b''.join([send_data, struct.pack('B', int(data[i: i + 2], 16))])
    print(send_data)

    # 通过socket广播出去，为避免失败，间隔广播三次
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        sock.sendto(send_data, (BROADCAST, 7))
        time.sleep(1)
        sock.sendto(send_data, (BROADCAST, 7))
        time.sleep(1)
        sock.sendto(send_data, (BROADCAST, 7))
        # return HTTPResponse()
        print("Done")
    except Exception as e:
        # return HTTPResponse()
        print(e)


# "DC-4A-3E-78-3E-0A"

mac = "B4-2E-99-6F-8F-D4"
wake_up(mac)