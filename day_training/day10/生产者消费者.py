

import threading, time
import queue

q = queue.Queue(maxsize=10)


def Producer(name):
    count = 1
    while True:
        q.put("包子 %s" % count)
        print("%s生产了包子%s" % (name, count))
        count += 1
        time.sleep(1)


def Consumer(name):
    while True > 0:
        print("[%s] 取到[%s]并且吃了它" % (name, q.get()))
        time.sleep(1)

p = threading.Thread(target=Producer, args=("ZCL",))
c = threading.Thread(target=Consumer, args=("ALEX",))
c1 = threading.Thread(target=Consumer, args=("CJY",))

p.start()
c.start()
c1.start()