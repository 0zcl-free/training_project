

import os,json
from conf import settings
from core import progress_bar


def client_put(self, *args):
    """
    用于处理客户端上传功能
    """
    cmd_split = args[0].split()  # 列表
    if len(cmd_split) > 1:
        filename = cmd_split[1]
        if os.path.isfile(filename):  # 判断是否存在文件
            file_size = os.stat(filename).st_size
            msg_dic = {             # 为了可拓展性，用字典形式
                "action": "put",  # 发送给服务端的指令
                "filename": filename,
                "file_size": file_size,
                "overridden": True
            }
            self.client.send(json.dumps(msg_dic).encode())
            # 防止粘包，等服务器确认
            # 可优化，确认同时服务端看客户端是否有权限等404 403(标准码)
            server_response = json.loads(self.client.recv(1024).decode())
            print(server_response)
            if server_response == settings.LOGIN_STATE["file_exit"] or\
                            server_response == settings.LOGIN_STATE["file_no_exit"]:
                f = open(filename, "rb")
                for line in f:  # 上传文件一行一行
                    self.client.send(line)
                    send_size = f.tell()   #获取当前指针位置（字节）
                    progress_bar.progress_bar(self, send_size, file_size)
                else:
                    print("file upload success")
                    f.close()
            #如果磁盘空间不足
            elif server_response == settings.LOGIN_STATE["size_empty"]:
                print("server_response:磁盘空间不足")

        else:
            print(filename, "is not exist")

