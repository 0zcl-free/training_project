from multiprocessing import Process, Manager
import os


def f(d, l):
    d[os.getpid()] = os.getpid()
    l.append(os.getpid())
    print(l)


if __name__ == '__main__':
    with Manager() as manager:
        d = manager.dict()   #生成可在多个进程间传递与共享的字典

        l = manager.list(range(5))  #生成可在多个进程间传递与共享的列表
        p_list = []
        for i in range(10):
            p = Process(target=f, args=(d, l))
            p.start()
            p_list.append(p)
        for res in p_list:  #等待结果
            res.join()

        print(d)
        print(l)

#进程间共享数据，不是传递
#不用加锁，manager已经自己内部加锁了，保证数据不乱，要将字典同时copy成好几份，表面是共享，实际上是copy多份