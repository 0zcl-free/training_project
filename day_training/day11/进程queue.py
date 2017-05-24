# #子进程返问父进程的队列,数据独立
# from multiprocessing import Process
# import queue
#
#
# def f():
#     q.put([42, None, 'hello'])
#
#
# if __name__ == '__main__':
#     q = queue.Queue()
#     p = Process(target=f,)  #子进程
#     p.start()
#     print(q.get())
#     p.join()



# #线程间的数据共享，子线程程放了一个数据，父线程打印数据
# from multiprocessing import Process
# import threading
# import queue
#
#
# def f():
#     q.put([42, None, 'hello'])
#
#
# if __name__ == '__main__':
#     q = queue.Queue()
#     p = threading.Thread(target=f,)  #子线程
#     p.start()
#     print(q.get())
#     p.join()


# 进程间的数据共享，子进程放了一个数据，父进程打印数据
# 在父进程生成队列q，子进程生成时父进程传q给它，能数据共享吗？
# from multiprocessing import Process
# import threading
# import queue   #线程queue
#
#
# def f(qq):
#     qq.put([42, None, 'hello'])
#
#
# if __name__ == '__main__':
#     q = queue.Queue()
#     p = Process(target=f, args=(q, ))  #子进程
#     p.start()
#     print(q.get())
#     p.join()
# #线程queue想传给子进程，传不了，想传的话必须得是进程Queue

#
# #好像进程间的数据共享Queue
from multiprocessing import Process, Queue  #进程Queue
import threading


def f(qq):
    qq.put([42, None, 'hello'])


if __name__ == '__main__':
    q = Queue()
    p = Process(target=f, args=(q, ))  #子进程
    p.start()
    print(q.get())
    p.join()

