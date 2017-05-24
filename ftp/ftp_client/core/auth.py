
"""
客户端身份验证
"""
from conf import settings
import hashlib

def send_auth(self):
    """
    发送用户名:密码到服务端，进行登陆验证
    :param self:
    :return: 返回400(成功)或200(失败)
    """
    user_name = input("Username:")
    password = input("Password:")
    #客户端发送用户名与密码(列表)
    password_hash = hash(password)
    user_data = "%s:%s" % (user_name, password_hash)
    self.client.send(user_data.encode())
    #接收服务端返回，认证成功True，认证失败False
    auth_recv = self.client.recv(1024).decode()
    if auth_recv == settings.LOGIN_STATE["auth_True"]:
        print("Welcome Login".center(50, "*"))
        return  auth_recv
    elif auth_recv == settings.LOGIN_STATE["auth_False"]:
        print("usename or password not exist")
        return auth_recv



def hash(data):
    #对密码进行md5加密
    m = hashlib.md5()
    m.update(data.encode())
    #返回加密后的数据
    return m.hexdigest()