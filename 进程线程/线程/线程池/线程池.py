# import time
# from concurrent.futures import ThreadPoolExecutor
#
# def task(url):
#     print('任务开始',url)
#     time.sleep(5)
#
# url_list = ['www.xxx-{}.com'.format(i) for i in range(100)]
#
# pool = ThreadPoolExecutor(10)#创建线程池，做多维护10个线程
#
# for url in url_list:
#     #在线程池中提交一个任务，线程池里面有空闲线程，就分配一个去执行，执行完后将线程交还给线程池，如果没有空闲的线程就等待
#     pool.submit(task,url)
#
# pool.shutdown(True) #等待线程池中的任务执行完成后再继续执行类似于t.join()
# print('end')


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
#     print('任务执行后的返回值',response.result())
#
# url_list = ['www.xxx-{}.com'.format(i) for i in range(50)]
#
# pool = ThreadPoolExecutor(10)#创建线程池，做多维护10个线程
# future_list = []
# for url in url_list:
#     #在线程池中提交一个任务，线程池里面有空闲线程，就分配一个去执行，执行完后将线程交还给线程池，如果没有空闲的线程就等待
#     future = pool.submit(task,url)
#     # future.add_done_callback(done)#再去执行利用task返回值的回调函数
#     future_list.append(future.result())#简单任务
# pool.shutdown(True) #等待线程池中的任务执行完成后再继续执行类似于t.join()
#
# for fu in future_list:
#     print(fu)

# 案例：下载图片保存到本地
import os
import requests
from concurrent.futures import ThreadPoolExecutor

def download(image_url):
    res = requests.get(url=image_url,headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'})
    return res

def outer(file_name):
    def save(response):
        res = response.result()
        if not os.path.exists('images'):
            os.makedirs('images')
        file_path = os.path.join('images', file_name)#拼接图片保存的位置(位置即图片名字)
        with open(file_path,'wb') as file:
            file.write(res.content)
    return save

pool = ThreadPoolExecutor(10)#创建线程池，最多维护10个线程

with open('mv.csv',mode='r',encoding='utf-8') as f:
    for line in f:
        name,url = line.split(",")
        file_name = "{}.png".format(name)
        fur = pool.submit(download,url)
        fur.add_done_callback(outer(file_name))#线程里开一个线程