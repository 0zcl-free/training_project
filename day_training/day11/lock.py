
from multiprocessing import Process, Lock


def f(l, i):
    l.acquire()
    print('hello world', i)
    l.release()


if __name__ == '__main__':
    lock = Lock()   #生成锁的实例

    for num in range(10):
        Process(target=f, args=(lock, num)).start()

#进程是独立的，为什么需要锁？？
#屏幕是共享的，加锁使打印不会乱。Windows 不会，Linux可能会乱。