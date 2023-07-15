# import threading
# loop = 1000000
# number = 0
# def add(count):
#     global number
#     for i in range(count):
#         number += 1
#
# def sub(count):
#     global number
#     for i in range(count):
#         number -= 1
#
# t1 = threading.Thread(target=add,args=(loop,))
# t2 = threading.Thread(target=sub,args=(loop,))
# t1.start()
# t2.start()
#
# t1.join()
# t2.join()
# print('number',number)

# import threading
#
# loop = 100000
# number = 0
#
# lock = threading.RLock()#创建锁
# def add(count):
#     lock.acquire() #申请锁
#     global number
#     for i in range(count):
#         number += 1
#     lock.release()#释放锁
#
# def sub(count):
#     lock.acquire()  # 申请锁
#     global number
#     for i in range(count):
#         number -= 1
#     lock.release()  # 释放锁
#
# t1 = threading.Thread(target=add, args=(loop,))
# t2 = threading.Thread(target=sub, args=(loop,))
# t1.start()
# t2.start()
#
# t1.join()
# t2.join()
# print('number', number)



# import threading
# num = 0
# lock = threading.RLock() #创建一把锁
##手动申请锁和释放锁
# def task():
#     lock.acquire()
#     global num
#     for i in range(1000000):
#         num += 1
#     print(num)
#     lock.release()

# import threading
# num = 0
# lock = threading.RLock() #创建一把锁
# #基于上下文管理with lock:   自动执行acquire和release
# def task():
#     with lock:
#         global num
#         for i in range(1000000):
#             num += 1
#     print(num)
# for i in range(2):
#     t = threading.Thread(target=task)
#     t.start()

#死锁现象，程序卡死
import threading
num = 0
lock = threading.Lock() #创建一把锁
def task():
    print('开始')
    lock.acquire()
    lock.acquire()
    global num
    for i in range(1000000):
        num += 1
    print(num)
    lock.release()
    lock.release()
for i in range(2):
    t = threading.Thread(target=task)
    t.start()