import time
import queue


def consumer(name):
    print("--->starting eating baozi...")
    while True:
        new_baozi = yield
        print("[%s] is eating baozi %s" % (name, new_baozi))
        # time.sleep(1)


def producer():
    r = con.__next__()
    r = con2.__next__()
    n = 0
    while n < 5:
        n += 1
        con.send(n)    #唤
        # 醒生成器并同时传给yield一个值
        con2.send(n)
        time.sleep(1)
        print("\033[32;1m[producer]\033[0m is making baozi %s" % n)


if __name__ == '__main__':
    con = consumer("c1")    #函数有yield，变成生成器，第一次不会执行，__next__才会执行
    con2 = consumer("c2")
    p = producer()