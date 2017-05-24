
import socketserver
import json,os
from core import deal_put
from core import deal_get
from core import deal_pwd
from core import deal_mkdir
from core import deal_cd
from core import deal_ls
from core import auth
from conf import settings


class MyTCPHandler(socketserver.BaseRequestHandler):  #继承父类
    def put(self, *args):
        deal_put.server_deal_put(self, *args)

    def get(self, *args):
        deal_get.server_deal_get(self, *args)

    def pwd(self, *args):
        deal_pwd.server_deal_pwd(self, *args)

    def mkdir(self, *args):
        deal_mkdir.server_deal_mkdir(self, *args)

    def ls(self, *args):
        deal_ls.server_deal_ls(self, *args)

    def cd(self, *args):
        deal_cd.server_deal_cd(self, *args)

    def handle(self):
        while True:
            #用户认证
            login_state = auth.auth_login(self)
            #如果认证成功
            if login_state == settings.LOGIN_STATE["auth_True"]:
                while True:
                    try:
                        self.data = self.request.recv(1024).strip()

                        print("{} wrote:".format(self.client_address[0]))
                        print(self.data)
                        cmd_dic = json.loads(self.data.decode())   #字典格式
                        action = cmd_dic["action"]      #获取客户端指令

                        if hasattr(self, action):   #反射
                            func = getattr(self, action)
                            func(cmd_dic)   #参数为字典格式
                        else:
                            print("服务端反射调用失败")

                    except ConnectionResetError as e:
                        print("客户端断开",e)
                        break
            elif login_state == settings.LOGIN_STATE["auth_False"]:
                continue


def run():
    #程序初始化时创建用户
    auth.create_user()
    #用户登陆时身份验证
    HOST, PORT = "localhost", 8787
    server = socketserver.ThreadingTCPServer((HOST, PORT), MyTCPHandler)  #实例化
    server.serve_forever()