
import socket

client = socket.socket() #声明socket类型,同时生成socket连接对象

client.connect(("localhost", 6969))  #连上本地6969端口
Flag = True
while Flag:
    msg = input(">>>:").strip()
    if len(msg) == 0:
        continue
    if msg == "exit":
        Flag = False
    client.send(msg.encode("utf-8"))
    data = client.recv(1024)  # 收1024个字节
    print("recv:", data.decode())


client.close()

#客户端断开，服务器端会曝错
#ConnectionResetError: [WinError 10054] 远程主机强迫关闭了一个现有的连接。