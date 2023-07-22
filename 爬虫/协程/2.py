import asyncio
import time
async def func1():
    print('你好，我是王建国')
    # time.sleep(4)   #出现同步操作，异步就中断了
    await asyncio.sleep(4)  #异步操作代码
    print('你好，我是王建国')

async def func2():
    print('你好，我是李雪琴')
    # time.sleep(3)
    await asyncio.sleep(3)
    print('你好，我是李雪琴')
async def func3():
    print('你好，我是潘金莲')
    # time.sleep(5)
    await asyncio.sleep(5)
    print('你好，我是潘金莲')

if __name__ == '__main__':
    start = time.time()
    f1 = asyncio.create_task(func1())#这样会报错，因为此时还没有时间循环
    f2 = func2()
    f3 = func3()
    #一次性启动多个任务（协程）
    tasks = [f1, f2, f3]
    asyncio.run(asyncio.wait(tasks))#想一次性执行多个异步任务时，需要把它们放在列表中，并且用asyncio的run函数中嵌套wait函数才能实现，它是固定搭配
    print(time.time() - start) #时间：最长的睡眠时间+调度时间


# import asyncio
# import time
# async def func1():
#     print('你好，我是王建国')
#     await asyncio.sleep(4)
#     print('你好，我是王建国')
# async def func2():
#     print('你好，我是李雪琴')
#     await asyncio.sleep(3)
#     print('你好，我是李雪琴')
# async def func3():
#     print('你好，我是潘金莲')
#     await asyncio.sleep(5)
#     print('你好，我是潘金莲')
# async def main():
#     tasks = [
#         asyncio.create_task(func1()),
#         asyncio.create_task(func2()),
#         asyncio.create_task(func3()),
#     ]#Task对象作用：是将多个任务放在事件循环里好做切换，一次性启动多个任务
#     await asyncio.wait(tasks)
# if __name__ == '__main__':
#     t1 = time.time()
#     asyncio.run(main())
#     print(time.time()-t1)#时间：最长的睡眠时间+调度时间


#在爬虫领域的应用
import asyncio
async def download(url):
    print('准备开始下载')
    await asyncio.sleep(2)#网络请求requests.get()这个是同步操作
    print('下载完成')

async def main():
    urls = [
        'https://www.baidu.com',
        'https://ww.bilibili.com',
        'https://www.163.com'
    ]
    tasks = []
    for url in urls:
        d = asyncio.create_task(download(url))
        tasks.append(d)
    await asyncio.wait(tasks)

if __name__ == '__main__':
    asyncio.run(main())