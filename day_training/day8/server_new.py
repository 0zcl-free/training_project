
import socket

server = socket.socket()

server.bind(("localhost", 6969))   #绑定要监听6969端口
server.listen(5)   #监听 5表示最多允许多少个连接

while True:
    print("等待客户端连接...")
    conn,addr = server.accept()  #等待 return sock(链接的实例), addr(对方地址)
    print("新连接", addr)
    Flag = True
    while Flag:
        data = conn.recv(1024)
        if data.decode() == "exit":
            print("客户连接断开...")
            Flag = False
        print("recv:", data.decode())
        conn.send(data.upper())

server.close()

