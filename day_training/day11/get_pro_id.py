
import multiprocessing
import os


def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())   #获得父进程号
    print('process id:', os.getpid())   #获得自己进程号
    print("\n\n")


def f(name):
    info('\033[31;1mcall from child process function f\033[0m')


if __name__ == '__main__':
    info('\033[32;1mmain process line\033[0m')
    p = multiprocessing.Process(target=f, args=('bob',))
    p.start()
    p.join()
