# from greenlet import greenlet
# def func1():
#     print(1) #2、输出1
#     gr2.switch() #3、切换到func2函数
#     print(2) #5、输出2
#     gr2.switch() #6、切换到func2函数
#
# def func2():
#     print(3) #4、输出3
#     gr1.switch() #4、切换到func1函数
#     print(4) #7、输出4
#
# gr1 = greenlet(func1)
# gr2 = greenlet(func2)
# gr1.switch() #1、执行func1函数




# import asyncio
# async def func():
#     print(1)
#     await asyncio.sleep(2)
#     print(2)
#     return '返回值'
# async def main():
#     print('main开始')
#     task_list = [
#         asyncio.create_task(func(),name='n1'),
#         asyncio.create_task(func(),name='n2'),
#     ]
#     print('main结束')
#     a,b = await asyncio.wait(task_list)#返回元组
#     print(a)
#     print(b)
# asyncio.run(main())
