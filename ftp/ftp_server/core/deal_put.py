


import os,json
from conf import settings
from core import get_dirsize


def server_deal_put(self, *args):
    """处理客户端上传文件的请求"""
    cmd_dic = args[0]       #字典格式
    filename = cmd_dic["filename"]
    file_size = cmd_dic["file_size"]
    file_path = os.path.join(self.current_path, filename)
    print("AA")
    dir_size = get_dirsize.get_dirsize(self.user_home_path)
    print("BB")
    print("当前用户磁盘空间大小:%s" % dir_size)
    #如果用户家目录下的大小加上本次将上传文件的大小仍小于最大的磁盘配额，则可以继续上传
    if dir_size+file_size < settings.MAX_SIZE:

        if os.path.isfile(file_path):     # 如果文件已经存在
            f = open(file_path + ".new", "wb")
            # 交互，防止粘包
            self.request.send(json.dumps(settings.LOGIN_STATE["file_exit"]).encode())
        else:  # 如果不存在，就上传
            f = open(file_path, "wb")
            self.request.send(json.dumps(settings.LOGIN_STATE["file_no_exit"]).encode())

        #self.request.send(b"200, OK")  # 可优化成字典json，状态码
        # 开始接收数据
        received_size = 0
        while received_size < file_size:
            data = self.request.recv(1024)
            received_size += len(data)
            f.write(data)
        else:  # 文件上传完成
            print("file [%s] has uploaded..." % filename)

    else:
        #磁盘配额不足
        self.request.send(json.dumps(settings.LOGIN_STATE["size_empty"]).encode())
