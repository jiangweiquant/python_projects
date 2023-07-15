import multiprocessing
# import time
# import os
# import threading
#
# def fun():
#     time.sleep(3)
#
# def task():
#     for i in range(10):
#         t = threading.Thread(target=fun)
#         t.start()
#     print(os.getpid(),os.getppid())
#     time.sleep(2)
#     print('进程名字:',multiprocessing.current_process().name)
#     print(len(threading.enumerate()))#获得子进程里面线程个数
# if __name__ == '__main__':
#     print(os.getpid())
#     p = multiprocessing.Process(target=task)
#     p.name = 'jw'
#     p.daemon = False
#     p.start()
#     print('主进程运行完成')


#cpu个数
count = multiprocessing.cpu_count()
print(count)
for i in range(count-1):#有一个主进程
    p = multiprocessing.Process()