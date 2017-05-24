
import time
import threading

event = threading.Event()   #生成event对象

def lighter():
    count = 0
    event.set()  #先设置为绿灯
    while True:
        if count > 5 and count < 10:  #改为红灯
            event.clear()  #清空标志位
            print("\033[41;1mread light is on...\033[0m")
        elif count > 10:
            event.set()   #设标志位，变绿灯
            count = 0
        else:
            print("\033[42;1mgreen light is on...\033[0m")

        time.sleep(1)
        count += 1


def car(name):
    #需要不断检测红绿灯
    while True:
        if event.is_set():  #若设置了标志位，代表绿灯
            print("\033[34;1m[%s] running...\033[0m" % name)
            time.sleep(1)
        else:
            print("\033[34;1m[%s] sees red light, waiting...\033[0m" % name)
            event.wait()
            print("\033[34;1m[%s] green light is on, start going...\033[0m" % name)


light = threading.Thread(target=lighter, )
light.start()

car1 = threading.Thread(target=car, args=("Tesla",))
car1.start()