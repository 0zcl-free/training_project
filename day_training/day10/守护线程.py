
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
    t.setDaemon(True)       #把当前线程设置为守护线程
    t.start()
    t_objs.append(t)

# for t in t_objs:
#     t.join()

print("----------all threads have finished", threading.current_thread(), threading.active_count())
print("cost:%s" % (time.time()-time_start))
#
# 守护线程(子线程)强制退出
#
# 主线程是非守护线程
# 应用：socket_server 每一个client链接过来，socket_server为链接为这个链接分配一个守护线程，
# 如果手动把socket_server停掉，client链接就全停掉了