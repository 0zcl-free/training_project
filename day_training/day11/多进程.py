
import multiprocessing
import threading
import time


def thread_run():
    print(threading.get_ident())  #打印线程号


def run(name):
    time.sleep(2)
    print('hello', name)
    t = threading.Thread(target=thread_run, )
    t.start()

if __name__ == '__main__':
    for i in range(10):
        p = multiprocessing.Process(target=run, args=('bob %s' % i,))
        p.start()       #起进程
