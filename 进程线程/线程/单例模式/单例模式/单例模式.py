# class Human:
#     instance = None
#     def __new__(cls, *args, **kwargs):##重载object内部自带的__new__,cls接收当前类
#         if cls.instance:
#             return cls.instance
#         cls.instance = object.__new__(cls)
#         return cls.instance
#
#     def __init__(self,name):
#         self.name = name
#
# one = Human('张三')
# print(one)
# two = Human('李四')
# print(two)


#用到线程去实例化对象
import threading
import time

class Human:
    instance = None
    lock = threading.RLock()
    def __new__(cls, *args, **kwargs):##重载object内部自带的__new__,cls接收当前类

        if cls.instance:#这个是后续为了再创建对象提高效率，不用再执行下面锁的管理以及判断【这段代码更好的优化了代码】
            return cls.instance

        with cls.lock:
            if cls.instance:
                return cls.instance
            # time.sleep(1)
            cls.instance = object.__new__(cls)
            return cls.instance

    def __init__(self,name):
        self.name = name

def task():
    obj = Human('X')
    print(obj)

for i in range(10):#创建10个线程
    t = threading.Thread(target=task)
    t.start()




