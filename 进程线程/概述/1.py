# import time
# import requests
# url_list = [('视频网站蓝光.mp4','https://www.baidu.com/link?url=8NhEgwwFx5sM3JNdSrz-MvnVFW8YOh2nGQn9eB9yUyVnYN5-03T1mFamWg77rCnwlagkEpNpnyliJNEJ5EcIY_&wd=&eqid=a29a7e44003195c90000000664a9a001'),
#             ('视频清晰度指南.mp4','https://www.baidu.com/link?url=8NhEgwwFx5sM3JNdSrz-MvnVFW8YOh2nGQn9eB9yUyVnYN5-03T1mFamWg77rCnwy4KiEP1bQAGaHRuCFq_FeK&wd=&eqid=a29a7e44003195c90000000664a9a001'),
#             ('微视频1.mp4','https://www.baidu.com/link?url=T4Qq9ATgVkbKuiD0gjD-uWkQo0YqWakyqXoZMildMNc_5Z-w9Y07ZuW7WxoYODRrnk0HA_f_pbS79f8wItMtHvGnWeZGPKLREYhxAZLENIW&wd=&eqid=a29a7e44003195c90000000664a9a001'),
#             ('微视频2.mp4','https://www.baidu.com/link?url=T4Qq9ATgVkbKuiD0gjD-uWkQo0YqWakyqXoZMildMNc_5Z-w9Y07ZuW7WxoYODRrnk0HA_f_pbS79f8wItMtHvGnWeZGPKLREYhxAZLENIW&wd=&eqid=a29a7e44003195c90000000664a9a001'),
#             ('微视频3.mp4','https://www.baidu.com/link?url=T4Qq9ATgVkbKuiD0gjD-uWkQo0YqWakyqXoZMildMNc_5Z-w9Y07ZuW7WxoYODRrnk0HA_f_pbS79f8wItMtHvGnWeZGPKLREYhxAZLENIW&wd=&eqid=a29a7e44003195c90000000664a9a001'),
#             ('微视频4.mp4','https://www.baidu.com/link?url=T4Qq9ATgVkbKuiD0gjD-uWkQo0YqWakyqXoZMildMNc_5Z-w9Y07ZuW7WxoYODRrnk0HA_f_pbS79f8wItMtHvGnWeZGPKLREYhxAZLENIW&wd=&eqid=a29a7e44003195c90000000664a9a001'),
#             ('微视频5.mp4','https://www.baidu.com/link?url=T4Qq9ATgVkbKuiD0gjD-uWkQo0YqWakyqXoZMildMNc_5Z-w9Y07ZuW7WxoYODRrnk0HA_f_pbS79f8wItMtHvGnWeZGPKLREYhxAZLENIW&wd=&eqid=a29a7e44003195c90000000664a9a001'),
#             ('微视频6.mp4','https://www.baidu.com/link?url=T4Qq9ATgVkbKuiD0gjD-uWkQo0YqWakyqXoZMildMNc_5Z-w9Y07ZuW7WxoYODRrnk0HA_f_pbS79f8wItMtHvGnWeZGPKLREYhxAZLENIW&wd=&eqid=a29a7e44003195c90000000664a9a001')]
# print('start_time',time.time())
# for name,url in url_list:
#     res = requests.get(url)
#     with open(name,mode='wb') as f:
#         f.write(res.content)
# print('end_time',time.time())


# import time
# import requests
# import threading
# url_list = [('视频网站蓝光.mp4','https://www.baidu.com/link?url=8NhEgwwFx5sM3JNdSrz-MvnVFW8YOh2nGQn9eB9yUyVnYN5-03T1mFamWg77rCnwlagkEpNpnyliJNEJ5EcIY_&wd=&eqid=a29a7e44003195c90000000664a9a001'),
#             ('视频清晰度指南.mp4','https://www.baidu.com/link?url=8NhEgwwFx5sM3JNdSrz-MvnVFW8YOh2nGQn9eB9yUyVnYN5-03T1mFamWg77rCnwy4KiEP1bQAGaHRuCFq_FeK&wd=&eqid=a29a7e44003195c90000000664a9a001'),
#             ('微视频1.mp4','https://www.baidu.com/link?url=T4Qq9ATgVkbKuiD0gjD-uWkQo0YqWakyqXoZMildMNc_5Z-w9Y07ZuW7WxoYODRrnk0HA_f_pbS79f8wItMtHvGnWeZGPKLREYhxAZLENIW&wd=&eqid=a29a7e44003195c90000000664a9a001'),
#             ('微视频2.mp4','https://www.baidu.com/link?url=T4Qq9ATgVkbKuiD0gjD-uWkQo0YqWakyqXoZMildMNc_5Z-w9Y07ZuW7WxoYODRrnk0HA_f_pbS79f8wItMtHvGnWeZGPKLREYhxAZLENIW&wd=&eqid=a29a7e44003195c90000000664a9a001'),
#             ('微视频3.mp4','https://www.baidu.com/link?url=T4Qq9ATgVkbKuiD0gjD-uWkQo0YqWakyqXoZMildMNc_5Z-w9Y07ZuW7WxoYODRrnk0HA_f_pbS79f8wItMtHvGnWeZGPKLREYhxAZLENIW&wd=&eqid=a29a7e44003195c90000000664a9a001'),
#             ('微视频4.mp4','https://www.baidu.com/link?url=T4Qq9ATgVkbKuiD0gjD-uWkQo0YqWakyqXoZMildMNc_5Z-w9Y07ZuW7WxoYODRrnk0HA_f_pbS79f8wItMtHvGnWeZGPKLREYhxAZLENIW&wd=&eqid=a29a7e44003195c90000000664a9a001'),
#             ('微视频5.mp4','https://www.baidu.com/link?url=T4Qq9ATgVkbKuiD0gjD-uWkQo0YqWakyqXoZMildMNc_5Z-w9Y07ZuW7WxoYODRrnk0HA_f_pbS79f8wItMtHvGnWeZGPKLREYhxAZLENIW&wd=&eqid=a29a7e44003195c90000000664a9a001'),
#             ('微视频6.mp4','https://www.baidu.com/link?url=T4Qq9ATgVkbKuiD0gjD-uWkQo0YqWakyqXoZMildMNc_5Z-w9Y07ZuW7WxoYODRrnk0HA_f_pbS79f8wItMtHvGnWeZGPKLREYhxAZLENIW&wd=&eqid=a29a7e44003195c90000000664a9a001')]
# def task(name,url):
#     res = requests.get(url)
#     with open(name,mode='wb') as f:
#         f.write(res.content)
#     print('end_time', time.time())
# print('start_time',time.time())
# for name,url in url_list:
#     #创建线程，让每个线程去执行task函数
#     t = threading.Thread(target=task,args=(name,url))
#     t.start()

import time
import requests
import multiprocessing
url_list = [('视频网站蓝光.mp4','https://www.baidu.com/link?url=8NhEgwwFx5sM3JNdSrz-MvnVFW8YOh2nGQn9eB9yUyVnYN5-03T1mFamWg77rCnwlagkEpNpnyliJNEJ5EcIY_&wd=&eqid=a29a7e44003195c90000000664a9a001'),
            ('视频清晰度指南.mp4','https://www.baidu.com/link?url=8NhEgwwFx5sM3JNdSrz-MvnVFW8YOh2nGQn9eB9yUyVnYN5-03T1mFamWg77rCnwy4KiEP1bQAGaHRuCFq_FeK&wd=&eqid=a29a7e44003195c90000000664a9a001'),
            ('微视频1.mp4','https://www.baidu.com/link?url=T4Qq9ATgVkbKuiD0gjD-uWkQo0YqWakyqXoZMildMNc_5Z-w9Y07ZuW7WxoYODRrnk0HA_f_pbS79f8wItMtHvGnWeZGPKLREYhxAZLENIW&wd=&eqid=a29a7e44003195c90000000664a9a001'),
            ('微视频2.mp4','https://www.baidu.com/link?url=T4Qq9ATgVkbKuiD0gjD-uWkQo0YqWakyqXoZMildMNc_5Z-w9Y07ZuW7WxoYODRrnk0HA_f_pbS79f8wItMtHvGnWeZGPKLREYhxAZLENIW&wd=&eqid=a29a7e44003195c90000000664a9a001'),
            ('微视频3.mp4','https://www.baidu.com/link?url=T4Qq9ATgVkbKuiD0gjD-uWkQo0YqWakyqXoZMildMNc_5Z-w9Y07ZuW7WxoYODRrnk0HA_f_pbS79f8wItMtHvGnWeZGPKLREYhxAZLENIW&wd=&eqid=a29a7e44003195c90000000664a9a001'),
            ('微视频4.mp4','https://www.baidu.com/link?url=T4Qq9ATgVkbKuiD0gjD-uWkQo0YqWakyqXoZMildMNc_5Z-w9Y07ZuW7WxoYODRrnk0HA_f_pbS79f8wItMtHvGnWeZGPKLREYhxAZLENIW&wd=&eqid=a29a7e44003195c90000000664a9a001'),
            ('微视频5.mp4','https://www.baidu.com/link?url=T4Qq9ATgVkbKuiD0gjD-uWkQo0YqWakyqXoZMildMNc_5Z-w9Y07ZuW7WxoYODRrnk0HA_f_pbS79f8wItMtHvGnWeZGPKLREYhxAZLENIW&wd=&eqid=a29a7e44003195c90000000664a9a001'),
            ('微视频6.mp4','https://www.baidu.com/link?url=T4Qq9ATgVkbKuiD0gjD-uWkQo0YqWakyqXoZMildMNc_5Z-w9Y07ZuW7WxoYODRrnk0HA_f_pbS79f8wItMtHvGnWeZGPKLREYhxAZLENIW&wd=&eqid=a29a7e44003195c90000000664a9a001')]
def task(name,url):
    res = requests.get(url)
    with open(name,mode='wb') as f:
        f.write(res.content)
    print('end_time', time.time())
if __name__ == '__main__':
    print('start_time',time.time())
    for name,url in url_list:
        #创建线程，让每个线程去执行task函数
        t = multiprocessing.Process(target=task,args=(name,url))
        t.start()



