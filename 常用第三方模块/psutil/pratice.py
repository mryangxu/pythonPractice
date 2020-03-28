import psutil
''' 获取cpu信息'''
print(psutil.cpu_count()) # cpu核心

print(psutil.cpu_count(logical=False)) # cpu物理核心

# 统计cpu的 用户 / 系统 / 空闲时间
print(psutil.cpu_times())

# top命令的cpu刷新率
for x in range(10):
    print(psutil.cpu_percent(interval=1, percpu=True))

