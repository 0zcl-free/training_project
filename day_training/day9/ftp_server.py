
import socket
import os
import hashlib

server = socket.socket()
server.bind(("localhost", 9998))

server.listen(5)

while True:
    conn,addr = server.accept()
    print("new conn:", addr)

    while True:
        print("等待新指令")
        data = conn.recv(1024)
        if not data:
            print("客户端已端开")
            break
        cmd, filename = data.decode().split()
        if os.path.isfile(filename):  #如果是文件
            f = open(filename, "rb")
            m = hashlib.md5()  # 创建md5对象
            file_size = os.stat(filename).st_size  #获取文件大小
            conn.send(str(file_size).encode())     #发送文件大小
            conn.recv(1024)       #接收客户端确认
            for line in f:
                conn.send(line)    #发送数据
                m.update(line)
            print(cmd, filename)
            print("file md5", m.hexdigest())
            f.close()
            conn.send(m.hexdigest().encode())  #发送md5

server.close()



# 问题：前面有conn.send(line)，现在又send(m.hexdigest())
# 有可能产生粘包，
# 客户端再给服务器一次响应？？不！来回交互太麻烦了
# 客户端已经知道接收多少数据，那让客户端接收文件时正好接收这些数据
# ＥＧ：原本是收5M，但服务端发了5.1M，多的0.1M是md5，
# 那在循环收文件时，收到5M就不再收，循环之后再recv就是md5

