# import time
# from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
#
# def task(url):
#     print('任务开始',url)
#     time.sleep(5)
#
# url_list = ['www.xxx-{}.com'.format(i) for i in range(10)]
# if __name__ == '__main__':
#     pool = ProcessPoolExecutor(4)
#     for url in url_list:
#         pool.submit(task,url)
#
#     pool.shutdown(True)
#     print('end')
import threading
# import multiprocessing
# import time
# from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
#
#
# def task(url):
#     print('任务开始', url)
#     time.sleep(2)
#     return url
#
# def done(res):
#     print(multiprocessing.current_process())
#     print(res.result())
#
#
# url_list = ['www.xxx-{}.com'.format(i) for i in range(10)]
# if __name__ == '__main__':
#     pool = ProcessPoolExecutor(4)
#     for url in url_list:
#         fur = pool.submit(task, url)
#         fur.add_done_callback(done)#这里与线程池有点区别，子进程去执行done函数，这里是主进程去执行done函数
#
#     pool.shutdown(True)
#     print(multiprocessing.current_process())
#     print('end')

#验证：这里与线程池有点区别，子进程去执行done函数，这里是主进程去执行done函数
# #任务完成后再做点其他事
# import time
# import random
# from concurrent.futures import ThreadPoolExecutor
#
# def task(url):
#     print('任务开始',url)
#     time.sleep(2)
#     return random.randint(0,10)
#
# def done(response):
#     print(threading.current_thread())
#     print('任务执行后的返回值',response.result())
#
# url_list = ['www.xxx-{}.com'.format(i) for i in range(50)]
#
# pool = ThreadPoolExecutor(10)#创建线程池，做多维护10个线程
# future_list = []
# for url in url_list:
#     #在线程池中提交一个任务，线程池里面有空闲线程，就分配一个去执行，执行完后将线程交还给线程池，如果没有空闲的线程就等待
#     future = pool.submit(task,url)
#     future.add_done_callback(done)#再去执行利用task返回值的回调函数
# pool.shutdown(True) #等待线程池中的任务执行完成后再继续执行类似于t.join()
# print(threading.current_thread())
# print('end')


#进程池里面资源共享时，创建锁。不能使用 lock = multiprocessing.RLock()，用Manager里面的Rlock/lock
from concurrent.futures import ProcessPoolExecutor
import multiprocessing
if __name__ == '__main__':
    pool = ProcessPoolExecutor(4)
    # lock = multiprocessing.RLock()#不能使用
    manager = multiprocessing.Manager()
    lock = manager.Rlock()