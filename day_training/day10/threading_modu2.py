
import threading
import time

class MyThread(threading.Thread):
    def __init__(self, n, sleep_time):
        super(MyThread,self).__init__()
        self.n = n
        self.sleep_time = sleep_time

    def run(self):   #用类方法必须写run
        print("running task", self.n)
        time.sleep(self.sleep_time)
        print("task done", self.n)


t1 = MyThread("t1",2)
t2 = MyThread("t2",4)

t1.start()
t2.start()
t1.join()   #卡住主程序
t2.join()
# 变成串行的了
print("main thread....")

#线程并行，所有子线程统一完毕再往主线程走
