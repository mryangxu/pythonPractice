import psutil
'''获取内存信息'''
print(psutil.virtual_memory()) # 物理内存
print(psutil.swap_memory()) # 交换内存
