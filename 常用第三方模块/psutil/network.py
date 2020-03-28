import psutil

'''网络信息'''

print('# 网络写字节数/包的个数')
print(psutil.net_io_counters())

print('# 获取网络接口信息')
print(psutil.net_if_addrs())

print('# 获取网络接口状态')
print(psutil.net_if_stats())

print('# 获取当前网络连接信息')
print(psutil.net_connections())