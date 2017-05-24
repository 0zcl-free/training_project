
import socket
import os
import hashlib

server = socket.socket()
server.bind(("localhost", 9999))

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
            print("file md5", m.hexdigest())
            f.close()
            conn.send(m.hexdigest().encode())  #发送md5

        print(cmd,filename)

server.close()



