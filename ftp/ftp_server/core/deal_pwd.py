import json
from conf import settings


def server_deal_pwd(self, *args):
    """ 用来处理客户端查看当前目录下的请求"""
    cmd_dic = args[0]  # 字典格式
    msg_dic = {
        "current_path":self.current_path,   #发送当前目录
        "cmd_state":settings.LOGIN_STATE["cmd_right"] #发送命令状态
    }
    self.request.send(json.dumps(msg_dic).encode())