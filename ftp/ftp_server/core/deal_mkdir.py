import json,os
from conf import settings


def server_deal_mkdir(self, *args):
    """处理用户在当前目录(家目录下)创建目录的请求"""
    cmd_dir = args[0]
    new_dir = cmd_dir["new_dir"]  #当前目录在将创建的目录
    new_dir_path = os.path.join(self.current_path, new_dir)
    print(new_dir_path)
    if not os.path.isdir(new_dir_path):
        #不存在目录，则创建
        print("new_dir no exit")
        os.popen("mkdir %s" % new_dir_path)
        msg_dic = {
            "cmd_state":settings.LOGIN_STATE["cmd_success"],
        }
        self.request.send(json.dumps(msg_dic).encode())
    else:
        msg = "%s:目录已存在，请先删除再创建" % settings.LOGIN_STATE["dir_exit"]
        self.request.send(json.dumps(msg).encode())
