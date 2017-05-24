
USER_LOGIN = {'is_login': False}

def outer(func):                   #装饰器
    def inner(*args, **kwargs):
        if USER_LOGIN['is_login']:
            r = func()
            return r
        else:
            print("请登陆")
    return inner


@outer
def change_pwd():
        print("欢迎%s修改密码".center(50, '-') % USER_LOGIN['current_user'])
        f = open('regist', 'r+', encoding='utf-8')
        for line in f:
            read_list = line.strip().split('|')
            if read_list[0] == USER_LOGIN['current_user']:
                new_pwd = input("请输入新的密码:")
                read_list[1] = new_pwd               #密码在列表中已更改，但需写到文件中去
                new_list = '|'.join(read_list)
                f.write(new_list + '\n')                    #结果是将已修改密码的记录加在最后一行，怎么把原来的删掉？
                f.close()
                print("修改密码成功".center(50, '-'))   #或者说，不加在最后一行，直接改那一行，又怎么做？
                break


@outer
def look_information():
        print("欢迎%s查看信息".center(50, '-') % USER_LOGIN['current_user'])
        f = open('regist', 'r+', encoding='utf-8')
        for line in f:
            read_list = line.strip().split('|')
            if read_list[0] == USER_LOGIN['current_user']:
                print("用户名:%s" % read_list[0])
                print("密码:%s" % read_list[1])
                print("邮箱:%s" % read_list[2])
                print("电话:%s" % read_list[3])
                f.close()


def login(user, pwd):
    f = open('regist', 'r+', encoding='utf-8')
    for line in f:
        read_list = line.strip().split('|')
        if read_list[0] == user and read_list[1] == pwd:    #若用户存在
            USER_LOGIN['is_login'] = True
            USER_LOGIN['current_user'] = user
            print("欢迎%s登陆".center(50, '-') % USER_LOGIN['current_user'])
            f.close()
            break

    if not USER_LOGIN['is_login']:
        print("用户不存在，请注册")



def register(reg_user, reg_pwd, reg_email, reg_phone):
    register_list = []
    register_list.append(reg_user)
    register_list.append(reg_pwd)
    register_list.append(reg_email)
    register_list.append(reg_phone)
    li = '|'.join(register_list)
    f = open('regist', 'a', encoding='utf-8')
    f.write(li + '\n')
    f.close()

    print("注册成功".center(50,'*'))



def main():

    while True:
        choice = input("请选择:1.登陆;2.注册;3.修改密码;4.查看信息：")
        if choice == '1':
            username = input("请输入用名名:")
            password = input("请输入密码:")
            login(username, password)
        elif choice == '2':
            regi_username = input("请输入注册用户名:")
            regi_pwd = input("请输入注册密码:")
            regi_email = input("请输入邮箱:")
            regi_phone = input("请输入电话:")
            register(regi_username, regi_pwd,regi_email,regi_phone)
        elif choice == '3':
            change_pwd()
        elif choice == '4':
            look_information()





main()