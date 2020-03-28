import psutil

'''获取磁盘信息'''


print(psutil.disk_partitions()) # 磁盘分区信息

print(psutil.disk_usage('/')) # 磁盘使用情况

print(psutil.disk_io_counters()) # 磁盘io

