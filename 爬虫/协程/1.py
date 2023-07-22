# import time
#
# def fun():
#     print('我爱黎明')
#     time.sleep(4)#当线程处于阻塞状态，cpu是不为工作的
#     print('我真的爱黎明')
#
# if __name__ == '__main__':
#     fun()


# input()
# requests.get() 在网络请求返回数据之前，程序也处于阻塞状态
# 一般情况下，当程序处于IO操作时，程序会处于阻塞状态

# 协程：当程序遇见IO操作时，可以选择性的切换到其他任务上【高效利用CPU】
# 多任务异步操作【在单线程条件下】

# python编写协程的程序
import asyncio
async def func():
    print("你好啊, 我叫赛利亚")


if __name__ == '__main__':
    g = func()  # 此时的函数是异步协程函数. 此时函数执行得到的是一个协程对象
    # print(g)
    asyncio.run(g)  # 协程程序运行需要asyncio模块的支持