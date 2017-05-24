
import socket
import os

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
        print("执行指令:", data.decode())
        cmd_res = os.popen(data.decode()).read()
        print("beford send", len(cmd_res))
        if len(cmd_res) == 0:   #输入不是指令，无返回会卡住
            cmd_res = "cmd has no output...wrong cmd..."


        conn.send(str(len(cmd_res.encode("utf-8"))).encode("utf-8"))  # 数字不能encode
        received = conn.recv(1024)
        print(received.decode())
        conn.send(cmd_res.encode("utf-8"))
        #尝试把数据一次性发给客户端，第一次没发完，把数据放在缓冲区，
        #下次再调用send时，先把缓冲区的数据发出去，新的数据再发到缓冲区
        #直到缓冲区满，自动发   （默认等缓冲区满再发）

        print("send done")

server.close()

#encode()默认是utf-8