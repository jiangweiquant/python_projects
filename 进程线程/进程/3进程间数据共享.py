from multiprocessing import Process,Value,Array,Manager,Queue,Pipe
'''Manager和Queue用的比较多'''
#1、Value,Array了解

# #2、Manager
# def f(d,l):
#     d[1] = '1'
#     d['2'] = 2
#     l.append(666)
#
# if __name__ == '__main__':
#     with Manager() as manager:
#         d = manager.dict({'name':'jw'})
#         l = manager.list([1,2])
#         p= Process(target=f,args=(d,l))
#         p.start()
#         p.join()
#         print(d)
#         print(l)

# #3、Queue
# def task(q):
#     for i in range(10):
#         q.put(i)
#
# if __name__ == '__main__':
#     queue = Queue()
#     p = Process(target=task,args=(queue,))
#     p.start()
#     p.join()
#     print('主进程')
#     print(queue.get())
#     print(queue.get())
#     print(queue.get())
#     print(queue.get())
#     print(queue.get())

#4、Pipe