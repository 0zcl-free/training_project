
import queue

q = queue.LifoQueue()  #last in first out 后进先出
q.put(1)
q.put(2)
q.put(3)
print(q.get())
print(q.get())
print(q.get())


# q = queue.PriorityQueue()
# q.put((10, "zcl"))
# q.put((5, "alex"))
# q.put((-5, "erirc"))
# q.put((15, "cjy"))
#
# print(q.get())
# print(q.get())
# print(q.get())
# print(q.get())