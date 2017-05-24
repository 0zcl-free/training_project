
import socket
import hashlib

client = socket.socket()

client.connect(("localhost", 9999))

while True:
    cmd = input(">>>:").strip()
    if len(cmd) == 0:
        continue
    if cmd.startswith("get"):
        client.send(cmd.encode())    #客户端发送指令
        receive_file_size = client.recv(1024)
        print("server file size",receive_file_size.decode())
        client.send("准备好接收文件了".encode())   #客户端发送确认

        receive_size = 0
        file_total_size = int(receive_file_size.decode())
        filename = cmd.split()[1]
        f = open(filename + ".new", "wb")   #新文件，没有的话会创建
        m = hashlib.md5()       #生成md5对象

        while receive_size < file_total_size:

            if file_total_size - receive_size > 1024:  #要收不止一次
                size = 1024
            else:  #最后一次，剩多少收多少
                size = file_total_size - receive_size
                print("最后一次收:", size)
            data = client.recv(size)

            receive_size += len(data)
            m.update(data)
            f.write(data)       #写到文件
        else:
            new_file_md5 = m.hexdigest() #根据收到文件生成的md5
            print("file recv done")
            print(receive_size, file_total_size)
            f.close()
        receive_file_md5 = client.recv(1024)
        print("server file md5:", receive_file_md5)
        print("client file md5:", new_file_md5)


client.close()