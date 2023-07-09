# #t.start()
# import threading
# loop = 100000000
# number = 0
#
# def add(count):
#     global number
#     for i in range(count):
#         number += 1
#
# t = threading.Thread(target=add,args=(loop,))
# t.start()
#
# print(number)
# '''
# 每次运行结果不一致。t.start线程准备好等待cpu调度，具体时间由CPU决定
# 主线程执行完后会等待子线程结束后最终程序结束
# '''


# #t.join()
# import threading
# loop = 100000000
# number = 0
#
# def add(count):
#     global number
#     for i in range(count):
#         number += 1
#
# t = threading.Thread(target=add,args=(loop,))
# t.start()
# t.join()#主线程等待子线程结束后再往后执行
# print(number)
# '''
# 主线程在t。join处等待子线程结束后再执行，最终程序结束
# 最后需等待一段时间后输出最终唯一结果100000000
# '''


# # t.daemon = Ture/False
# import threading
# import time
# def task():
#     time.sleep(5)
#     print('任务')
# t = threading.Thread(target=task)
# t.daemon = True
# t.start()
# print('END')
# '''
# 设置为True，主线程结束子线程也自动关闭
# 运行结果：
#     END
# 设置为False，主线程执行完后等待子线程结束，最终结束程序（默认）
# 运行结果：
#     END
#     任务
# '''

# # 线程名字的设定和获取
# import threading
# def task():
#     #获取当前执行此代码的线程
#     name = threading.current_thread().name
#     print(name)
#
# for i in range(10):
#     # t = threading.Thread(target=task, name='日莫-{}'.format(i))
#     t = threading.Thread(target=task)
#     # t.setName('日莫-{}'.format(i))
#     t.start()

# 自定义线程类继承threading.Thread.直接将线程要做的是封装成函数写在里面，创建一个对象t，再t.start即可
import threading
class MyThread(threading.Thread):
    def run(self):
        print('执行此线程')

t = MyThread() #创建实例对象
t.start()