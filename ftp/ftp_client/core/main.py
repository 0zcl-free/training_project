
import socket
import hashlib
import os
import json
from core import interactive
from core import put
from core import get
from core import auth
from conf import settings
from core import pwd
from core import mkdir
from core import ls
from core import cd

class FtpClient(object):
    def __init__(self):
        self.client = socket.socket()

    def help(self):
        msg = """
        ls
        pwd
        cd ../..
        get filename
        put filename
        """
        print(msg)

    def connect(self, ip, port):
        self.client.connect((ip, port))


    def interactive(self):   #交互
        interactive.interactive(self
)

    def cmd_put(self, *args):  #*args是为了将来参数的拓展
        put.client_put(self, *args)

    def cmd_get(self, *args):
        get.client_get(self, *args)

    def send_auth_data(self):
        #返回用户帐号名与密码
        login_state = settings.LOGIN_STATE["auth_False"]
        while login_state != settings.LOGIN_STATE["auth_True"]:
            login_state = auth.send_auth(self)

    def cmd_pwd(self, *args):
        pwd.client_pwd(self, *args)

    def cmd_mkdir(self, *args):
        mkdir.client_mkdir(self, *args)

    def cmd_ls(self, *args):
        ls.client_ls(self, *args)

    def cmd_cd(self, *args):
        cd.client_cd(self, *args)


def run():
    ftp_client = FtpClient()
    ftp_client.connect("localhost", 8787)
    #身份验证
    ftp_client.send_auth_data()
    #客户端与服务端交户
    ftp_client.interactive()
