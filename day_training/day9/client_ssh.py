
import socket

client = socket.socket()

client.connect(("localhost", 9999))

while True:
    cmd = input(">>>:").strip()
    if len(cmd) == 0:
        continue
    client.send(cmd.encode("utf-8"))
    cmd_res_size = client.recv(1024)   #接受命令结果的长度
    print("命令结果大小:", cmd_res_size.decode())
    client.send("准备好接收，可以发了...".encode("utf-8"))

    received_size = 0
    received_data = b""
    # 收到的大小与实际大小不等就一直收
    while received_size < int(cmd_res_size.decode()):
        data = client.recv(1024)
        # 每次收到的有可能小于1024，所以必须有len判断
        received_size += len(data)
        #print(data.decode())
        print(received_size)
        received_data += data
    else:
        print("cmd_res receive done...", received_size)
    print(received_data.decode())
    #cmd_res = client.recv(1024)
    #print(cmd_res.decode())

client.close()