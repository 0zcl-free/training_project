import selectors
import socket

#默认用epoll
sel = selectors.DefaultSelector()  #sel对象


def accept(sock, mask):
    conn, addr = sock.accept()  # Should be ready
    print('accepted', conn, 'from', addr)
    conn.setblocking(False)
    #新年连接注岫read回调函数
    sel.register(conn, selectors.EVENT_READ, read)


def read(conn, mask):
    data = conn.recv(1024)  # Should be ready
    if data:
        print('echoing', repr(data), 'to', conn)
        conn.send(data)  # Hope it won't block
    else:
        print('closing', conn)
        sel.unregister(conn)   #取消注册
        conn.close()


sock = socket.socket()
sock.bind(('localhost', 10000))
sock.listen(100)
sock.setblocking(False)
#将sock注册到sel,进行监听;只要来一个新连接，就调用accept函数
sel.register(sock, selectors.EVENT_READ, accept)

while True:
    #默认阻塞，有活动连接就返回活动的连接列表
    events = sel.select()   #返回列表
    for key, mask in events:
        callback = key.data   #相当于调accept
        callback(key.fileobj, mask)  #key.fileob相当于文件句柄