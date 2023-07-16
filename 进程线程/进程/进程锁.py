import multiprocessing
import time

def task(lock):
    print('开始')
    lock.acquire()
    with open('f1.txt','r') as f:
        current_num = int(f.read())
    print('排队抢票了')
    time.sleep(0.5)
    current_num -= 1
    with open('f1.txt', 'w') as f:
        f.write(str(current_num))
    lock.release()

if __name__ == '__main__':
    lock = multiprocessing.RLock()#创建进程锁，进程锁可以进行传递，线程锁不能
    for i in range(10):
        p = multiprocessing.Process(target=task,args=(lock,))
        p.start()
