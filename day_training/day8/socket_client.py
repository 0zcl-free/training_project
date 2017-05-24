
import socket

#默认(self, family=AF_INET, type=SOCK_STREAM, proto=0, fileno=None)
client = socket.socket() #声明socket类型,同时生成socket连接对象

client.connect(("localhost", 6969))  #连上本地6969端口

client.send(b"Hello World!")

data = client.recv(1024)   #收1024个字节
print("recv:", data)
client.close()

