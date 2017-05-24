
import os,json
from conf import settings
from core import progress_bar

def client_get(self, *args):
    """
    用来处理客户端下载功能
    """
    cmd_split = args[0].split()
    if len(cmd_split) > 1:
        filename = cmd_split[1]
        msg_dic = {             # 为了可拓展性，用字典形式
            "action": "get",  # 发送给服务端的指令
            "filename": filename,
            "overridden": True
        }
        self.client.send(json.dumps(msg_dic).encode())
        # 防止粘包，等服务器确认
        # 可优化，确认同时服务端看客户端是否有权限等404 403(标准码)
        server_response = json.loads(self.client.recv(1024).decode())
        print(server_response,type(server_response))
        if server_response["file_exit"] == settings.LOGIN_STATE["file_exit"]:
            self.client.send("客户端已准备好下载".encode())
            if os.path.isfile(msg_dic["filename"]):    #文件已经存在
                f = open(filename + ".new", "wb")
            else:
                f = open(filename, "wb")
            receive_size = 0
            while receive_size < server_response["file_size"]:
                data = self.client.recv(1024)
                receive_size += len(data)
                #调用progress_bar模块的方法
                progress_bar.progress_bar(self, receive_size, server_response["file_size"])
                f.write(data)
            else:
                print("download from server success")

        elif server_response["file_exit"] == settings.LOGIN_STATE["file_no_exit"]:
            print("%s:请求文件不存在" % server_response["file_exit"])





