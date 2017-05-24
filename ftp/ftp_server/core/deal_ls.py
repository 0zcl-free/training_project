import os,json

def server_deal_ls(self, *args):
    """完成用户显示当前目录下文件(包括目录)的请求"""
    cmd_dic = args[0]
    r = os.popen("dir %s" % self.current_path)
    dir_message = r.read()
    self.request.send(dir_message.encode())
