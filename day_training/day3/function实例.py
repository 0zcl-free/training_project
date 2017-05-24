def login(username, password):
    """                         #双引号
    用于用户登陆
    :param username: 用户输入的用户名
    :param password: 用户输入的密码
    :return: true 表示登陆成功  false 表示登陆失败
    """
    f = open('db', 'r')
    for line in f:              #一行一行读文件
        line_list = line.split('|')
        if line_list[0] == username and line_list[1] == password:
            return True
    return False


def register(username, password):   #函数与函数之间空两行！规范
    """
    用于
    :param username:
    :param password:
    :return:
    """
    f = open('db','a')
    temp = '\n' + username + '|' + password
    f.write(temp)
    f.close()


def main():
    t = int(input('1:登陆; 2:注册'))
    if t == 1:
        user = input("Username:")
        passd = input("Password:")
        r = login(user, passd)
        if r == True:
            print("登陆成功")
        else:
            print("登陆失敗")
    elif t == 2:
        user = input("Username:")
        passd = input("Password:")
        register(user, passd)
        print("注册成功")

main()