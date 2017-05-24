
USER_INFO = {}
USER_INFO['is_login'] = True
USER_INFO['user_type'] = 2

def check_login(func):
    def inner(*args, **kwargs):
        if USER_INFO.get('is_login', None):
            ret = func(*args, **kwargs)
            return ret
        else:
            print("please login")
    return inner

def check_admin(func):
    def inner(*args, **kwargs):
        if USER_INFO.get("user_type", None) == 2:
            ret = func(*args, **kwargs)
            return ret
        else:
            print("无管理员权限")
    return inner

@check_login
@check_admin
def index():
    print("index")



index()