
import threading
import time

def run(n):     #run 随便起的名
    print("task", n)
    time.sleep(2)
    print("task done", n, threading.current_thread())

time_start = time.time()
t_objs = []
for i in range(50):
    t = threading.Thread(target=run, args=("t-%s" % i,)) #要加逗号
    t.start()
    t_objs.append(t)
print("******",threading.active_count())
for t in t_objs:
    t.join()

print("----------all threads have finished", threading.current_thread(), threading.active_count())
print("cost:%s" % (time.time()-time_start))
