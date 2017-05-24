
LOGIN_USER = {'is_login': False}

def outer(func):      #装饰器最常用  权限验证！
    def inner(*args, **kwargs):
        if LOGIN_USER['is_login']:
            r = func()
            return r
        else:
            print('请登陆'.center(50, '-'))
    return inner


@outer
def order():
    print("欢迎%s登陆" % LOGIN_USER['current_user'])

@outer
def change():
     print("欢迎%s登陆" % LOGIN_USER['current_user'])

@outer
def manager():
     print("欢迎%s登陆" % LOGIN_USER['current_user'])



def login(user, pwd):
    if user == 'zcl' and pwd == '123':
        LOGIN_USER['is_login'] = True
        LOGIN_USER['current_user'] = user
        manager()


def main():
    while True:
        inp = input('1.后台管理;2.登陆;3.修改;4.订单')
        if inp == '1':
            manager()
        elif inp == '2':
            username = input('请输入用户名：')
            password = input('请输入密码:')
            login(username, password)
        elif inp == '3':
            change()
        elif inp == '4':
            order()



main()