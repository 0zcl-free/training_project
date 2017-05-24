
import socket
import hashlib

client = socket.socket()

client.connect(("localhost", 9998))

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
            data = client.recv(1024)
            receive_size += len(data)
            m.update(data)
            f.write(data)       #写到文件
        else:
            new_file_md5 = m.hexdigest() #根据收到文件生成的md5
            print("file recv done")
            print("receive_size:", receive_size)
            print("total_file_size:", file_total_size)
            f.close()
        receive_file_md5 = client.recv(1024)
        print("server file md5:", receive_file_md5)
        print("client file md5:", new_file_md5)


client.close()


# 最后一次可能粘包
# EG：文件大小是50000KB，倒数第二次收到49800，剩下200，
# 最后一次还是收1024，若服务器有发多余的数据就超了，产生粘包！
# 解决：最后一次判断还剩多少，直接收剩下的！