
from multiprocessing import Process, Pipe


def f(conn):
    conn.send([42, None, 'hello from child'])
    conn.send([42, None, 'hello from child2'])
    print("from parent:", conn.recv())
    conn.close()


if __name__ == '__main__':
    parent_conn, child_conn = Pipe()  #生成管道实例(管道的两边)
    p = Process(target=f, args=(child_conn,))
    p.start()
    print(parent_conn.recv())
    print(parent_conn.recv())
    parent_conn.send("ZCL NO.1")
    p.join()

