''' 获取进程信息'''
import psutil

# 所有进程id
print(psutil.pids())

# 获取指定进程
# print(psutil.Process(3780))

for i in psutil.pids():
    p = psutil.Process(i)
    if 'python' in str(p.name):  # name 进程名称
        print('进程exe路径')
        print(p.exe())

        print('进程工作目录')
        print(p.cwd())

        print('进程启动命令行')
        print(p.cmdline())

        print('父进程id')
        print(p.ppid())

        print('父进程')
        print(p.parent())

        print('子进程列表')
        print(p.children())

        print('进程状态')
        print(p.status())

        print('进程用户名')
        print(p.username())

        print('进程创建时间')
        print(p.create_time())

        print('进程终端')
        # print(p.terminal())

        print('进程使用的cpu时间')
        print(p.cpu_times())

        print('进程的创建时间')
        print(p.create_time())

        print('进程使用的内存')
        print(p.memory_info())

        print('进程打开的文件')
        print(p.open_files())

        print('进程相关网路连接')
        print(p.connections())

        print('进程的线程数量')
        print(p.num_threads())

        print('所有线程信息')
        print(p.threads())

        print('进程环境变量')
        print(p.environ())

        print('结束进程')
        print(p.terminate())

        # print(p)
    # print(psutil.Process(i))