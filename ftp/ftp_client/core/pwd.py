
import json
from conf import settings

def client_pwd(self, *args):
    """用来查看用户当前的目录"""
    cmd_split = args[0].split()
    if len(cmd_split) == 1 and cmd_split[0] == "pwd":
        msg_dic = {
            "action":"pwd",
        }
        self.client.send(json.dumps(msg_dic).encode())
        server_response = json.loads(self.client.recv(1024).decode())
        print(server_response)
        print(server_response["current_path"])
    else:
        print("%s:命令错误" % settings.LOGIN_STATE["cmd_error"])