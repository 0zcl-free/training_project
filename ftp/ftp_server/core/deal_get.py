import os,json
from conf import settings

def server_deal_get(self, *args):
    """处理客户端下载文件的请求"""
    cmd_dic = args[0]
    filename = cmd_dic["filename"]
    if os.path.isfile(filename):
        file_size = os.stat(filename).st_size #服务端文件大小
        msg_dic = {
            "file_size":file_size,  #服务端将发给客户端的文件的大小
            "file_exit":settings.LOGIN_STATE["file_exit"]
        }
        self.request.send(json.dumps(msg_dic).encode())
        #防止粘包，服务端与客户端再进行一次交互
        client_response = self.request.recv(1024)
        print(client_response.decode())
        f = open(filename, "rb")
        for line in f:
            self.request.send(line)
        else:
            print("server:file upload to client success")
    else:
        msg_dic = {"file_exit":settings.LOGIN_STATE["file_no_exit"]}
        self.request.send(json.dumps(msg_dic).encode())
