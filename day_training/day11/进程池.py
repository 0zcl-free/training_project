
from  multiprocessing import Process, Pool
import time,os


def Foo(i):
    time.sleep(2)
    print("in process", os.getpid())
    return i + 100


def Bar(arg):
    print('-->exec done:', arg, os.getpid())


if __name__ == "__main__":
    pool = Pool(processes=5)  #允许进程池同时放入5个进程
    print("主进程ID: ", os.getpid())
    for i in range(10):
        # 并行  callback 回调:执行完Foo,就执行Bar;Foo执行不完，就不执行Bar;是主进程执行的回调
        pool.apply_async(func=Foo, args=(i,), callback=Bar)
        #pool.apply(func=Foo, args=(i,))    #串行

    print('end')
    pool.close()
    pool.join()  # 进程池中进程执行完毕后再关闭，如果注释join，那么程序直接关闭。