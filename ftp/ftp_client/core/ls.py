import json


def client_ls(self, *args):
    """查看当前目录下的文件(包括目录)"""
    cmd_split = args[0].split()
    if len(cmd_split) == 1 and cmd_split[0] == "ls":
        msg_dic = {
            "action":"ls",
        }
        self.client.send(json.dumps(msg_dic).encode())
        server_response = self.client.recv(1024)
        print(server_response.decode())