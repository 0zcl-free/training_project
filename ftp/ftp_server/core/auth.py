
"""
用户加密认证，登陆模块
"""
import os,sys,hashlib
import json
from conf import settings
from core import db_handle


def auth_login(self):
    """用户登陆时调用"""
    recv_data = self.request.recv(1024).strip()
    recv_data = recv_data.decode()
    print(recv_data,type(recv_data))
    recv_list = recv_data.split(":")
    print(recv_list)
    # 登陆后用户当前目录, 即用户的家目录
    self.current_path = os.path.join(settings.HOME_PATH, recv_list[0])
    # 用户宿主目录
    self.user_home_path = os.path.join(settings.HOME_PATH, recv_list[0])

    user_path = "%s/data/%s.json" % (settings.PATH, recv_list[0])
    print(user_path)
    if os.path.isfile(user_path):
        print("user(file) exist")
        file_data = db_handle.user_load(user_path)
        print(file_data)
        if file_data["password"] == recv_list[1]:
            print("login success")
            #发送状态码给客户端
            self.request.send(settings.LOGIN_STATE["auth_True"].encode())
            print("send login_state")
            #认证成功的状态码
            return settings.LOGIN_STATE["auth_True"]
        else:
            #发送状态码给客户端
            self.request.send(settings.LOGIN_STATE["auth_False"].encode())
            print("send login_state")
            #认证失败的状态码
            return settings.LOGIN_STATE["auth_False"]
    else:
        # 发送状态码给客户端
        self.request.send(settings.LOGIN_STATE["auth_False"].encode())
        print("send login_state")
        print("False,please registe")
        return settings.LOGIN_STATE["auth_False"]


def create_user():
    #服务端初始化时，先创建两个用户Alex,zcl
    path = settings.PATH
    for key in settings.USER_DATA:
        print(settings.USER_DATA)
        user_path = "%s/data/%s.json" % (path, key)
        if not os.path.isfile(user_path):
            password_hash = hash(settings.USER_DATA[key])
            user_data = {
                "username":key,
                "password":password_hash,
                "user_path":os.path.join(settings.HOME_PATH, key),  #创建同时添加用户个人目录
                "max_size": settings.MAX_SIZE      #磁盘配额100M
            }
            #json.dump(user_data, open(user_path,"w",encoding="utf-8"))
            db_handle.user_dump(user_path, user_data)
    user_mkdir()


def user_mkdir():
    """创建用户个人目录，在home目录下"""
    for key in settings.USER_DATA:
        user_home_path = os.path.join(settings.HOME_PATH, key)
        if not os.path.isdir(user_home_path):
            os.popen("mkdir %s" % user_home_path)


def hash(data):
    m = hashlib.md5()
    m.update(data.encode())
    #返回加密后的数据
    return m.hexdigest()