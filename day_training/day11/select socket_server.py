#单线程下的多路复用

import select
import socket
import queue

server = socket.socket()
server.bind(("localhost", 9000))
server.listen(1000)

#设置为非阻塞模式
server.setblocking(False)
msg_dic = {}

inputs = [server, ]     #交给select（内核）监控
outputs = []

while True:
    #第一个inputs:想让内核监测的连接 eg:100个连接有1个活动就返回100个
    #第二个inputs:出异常的连接(断了) eg:让内核监测100个连接，返回有问题的连接
    #往outputs放连接，则下次select返回
    #readable:新来的连接 exceptional:出异常的连接
    readable, writeable, exceptional = select.select(inputs, outputs, inputs)
    print(readable, writeable, exceptional)

    for r in readable:
        if r is server:  #代表来了一个新连接
            conn, addr = server.accept()
            print("来了个新连接", addr)
            #因为这个新建立的连接还没发数据，现在就接收程序就会爆错
            #要想实现这个客户端发数据来时server端能知道，就需要让select再监测这个conn
            inputs.append(conn)
            # 来个新连接，初始化一个队列，存返回给客户端的数据
            msg_dic[conn] = queue.Queue()
        else:      #代表之前的连接发数据来了
            data = r.recv(1024)
            print("recv:", data)
            msg_dic[r].put(data)
            #放入返回的连接队列里
            outputs.append(r)

    for w in writeable:   #要返回给客户端的连接列表
        data_to_client = msg_dic[w].get()
        w.send(data_to_client)   #返回客户端源数据
        outputs.remove(w)  #确保下次循环时writeable不返回已经处理完的连接

    for e in exceptional:
        if e in outputs:
            outputs.remove(e)
        inputs.remove(e)

        del  msg_dic[e]   #删除队列