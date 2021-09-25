import threading

import time

# 进程：正在运行的应用程序，程序一旦开始运行就是进程，是cpu资源分配的最小单元，每个进程都有自己的资源空间，互不影响
# 线程：依托在进程中，是cpu调度的最小单元，同一个进程中的不同线程是共享资源空间，所以不同线程之间切换资源消耗较小，但是由于是共享资源，在对同一个资源进行处理的时候，容易因为代码不当，出现死锁等情况
# 产生死锁的四个条件
# 1.互斥性：
# 同一个资源，每次都只能被一个线程持有
# 2.不可剥夺性：
# 线程所获得得资源在未使用完之前，不得被其他线程剥夺，只能自己主动释放
# 3.请求与保持：
# 线程已经获得了资源a，但是资源b因为被其他线程所持有，一直不释放，此时请求线程被阻塞，但对自己获得的资源a也不进行释放
# 4.循环等待
# 链中每一个线程已获得的资源同时被 链中下一个进程所请求

class MyThread(threading.Thread):
    global num
    mutex = threading.Lock()

    def run(self):
        time.sleep(1)
        if self.mutex.acquire(1):
            num = num+1
            msg = self.name + ' set num to ' + str(num)
            print(msg)

            mutex.acquire()

            mutex.release()

            mutex.release()

            num = 0



def test():
    for i in range(5):
        t = MyThread()
        t.start()

if __name__ == '__main__':

    test()