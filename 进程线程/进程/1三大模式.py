# #fork[在windows上无法运行]
# import multiprocessing
# def task():
#     print(name)#[]
# if __name__ == '__main__':
#     multiprocessing.set_start_method('fork')##在windows电脑上运行不了
#     name = []
#     p1 = multiprocessing.Process(target=task)
#     p1.start()

# import multiprocessing
# def task():
#     print(name)#[123]
# if __name__ == '__main__':
#     multiprocessing.set_start_method('fork')##在windows电脑上运行不了
#     name = []
#     name.append(123)
#     p1 = multiprocessing.Process(target=task)
#     p1.start()

#spawn模式
import multiprocessing
import time

# def task():
#     print(name)
# if __name__ == '__main__':
#     multiprocessing.set_start_method('spawn')
#     name = []
#     p1 = multiprocessing.Process(target=task)
#     p1.start()
'''NameError: name 'name' is not defined'''

# def task(data):
#     print(data)
# if __name__ == '__main__':
#     multiprocessing.set_start_method('spawn')
#     name = []
#     p1 = multiprocessing.Process(target=task,args=(name,))
#     p1.start()
#     name.append(123)
#     time.sleep(2)
#     print(name)


#forkserver
# import multiprocessing
# import time
# def task(): #报错：name未定义
#     print(name)
# if __name__ == '__main__':
#     multiprocessing.set_start_method('forkserver')
#     name = []
#     p1 = multiprocessing.Process(target=task)
#     p1.start()
import multiprocessing
import time
def task(data): #[]
    print(data)
if __name__ == '__main__':
    multiprocessing.set_start_method('forkserver')
    name = []
    p1 = multiprocessing.Process(target=task,args=(name,))
    p1.start()