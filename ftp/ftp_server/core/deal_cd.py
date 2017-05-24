import json,os
from conf import settings

def server_deal_cd(self, *args):
    """处理用户切换目录的功能"""
    cmd_dic = args[0]
    cd_dir = cmd_dic["cd_dir"]
    dir_path = self.current_path + r"%s" % cd_dir
    if cd_dir == ".." and len(self.current_path) > len(self.user_home_path):
        #返回上一级目录
        self.request.send(json.dumps(settings.LOGIN_STATE["cmd_success"]).encode())
        self.current_path = os.path.dirname(self.current_path)
    elif os.path.isdir(dir_path):   #切换目录
        if cd_dir != "." and cd_dir != "..":
            self.request.send(json.dumps(settings.LOGIN_STATE["cmd_success"]).encode())
            self.current_path = self.current_path + r"%s" % cd_dir
            print(self.current_path)
        else:
            self.request.send(json.dumps(settings.LOGIN_STATE["cmd_fail"]).encode())
    else:   #切换的目录不存在
        self.request.send(json.dumps(settings.LOGIN_STATE["dir_no_exit"]).encode())


