
import socket

server = socket.socket()

server.bind(("localhost", 6969))   #绑定要监听6969端口
server.listen(5)   #监听

conn,add = server.accept()  #等待 return sock(链接的实例), addr(对方地址)
print(conn,add)
#conn就是客户端连接过来而在服务器端为其生成的一个连接实例
data = conn.recv(1024)
print("recv:", data)
conn.send(data.upper())

server.close()

#python3只能发bytes类型