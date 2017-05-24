import shutil
import os
import sys


USER_LOGIN = {'is_login': False}

def outer(func):                   #装饰器,若没有登陆则输出“请登陆”
    def inner(*args, **kwargs):
        if USER_LOGIN['is_login']:
            r = func(*args, **kwargs)
            return r
        else:
            print("请登陆")
    return inner


def outer1(func):                 #装饰器,若不是管理员则输出“权限不足”
    def inner1(*args, **kwargs):
        if USER_LOGIN['user_type'] == '2':
            r = func(*args, **kwargs)
            return r
        else:
            print("不是管理员,权限不足")
    return inner1


@outer
def change_pwd(changed_user, changed_pwd, type_user):         #修改密码
    if type_user == '1':
        print("欢迎%s修改密码".center(50, '-') % USER_LOGIN['current_user'])
        with open('regist', 'r', encoding='utf-8') as f1, open('regist_new', 'w', encoding='utf-8') as f2:
            for line in f1:
                read_list = line.strip().split('|')
                if read_list[0] == changed_user:
                    read_list[1] = changed_pwd
                    f2.write('|'.join(read_list) + '\n')
                    continue

                f2.write(line)
        shutil.move('regist', 'regist_bak')           #把regist文件复制到regist_bak文件中去
        os.rename('regist_new', 'regist')             #再将regist_new改名为regist            妙妙妙！
    else:
        print("没有权限修改管理员密码")



@outer
def look_information():           #查看本用户信息
    print("欢迎%s查看信息".center(50, '-') % USER_LOGIN['current_user'])
    with open('regist', 'r+', encoding='utf-8') as f:
        for line in f:
            read_list = line.strip().split('|')
            if read_list[0] == USER_LOGIN['current_user']:
                print("用户名:%s" % read_list[0])
                print("密码:%s" % read_list[1])
                print("邮箱:%s" % read_list[2])
                print("电话:%s" % read_list[3])



def login(user, pwd):         #登陆
    with open('regist', 'r+', encoding='utf-8') as f:
        for line in f:
            read_list = line.strip().split('|')
            if read_list[0] == user and read_list[1] == pwd:    #若用户存在
                USER_LOGIN['is_login'] = True
                USER_LOGIN['current_user'] = user
                USER_LOGIN['user_type'] = read_list[-1]
                print("欢迎%s登陆".center(50, '-') % USER_LOGIN['current_user'])
                break

    if not USER_LOGIN['is_login']:        #若用户还没注册
        print("用户不存在，请注册")



def register(reg_user, reg_pwd, reg_email, reg_phone):         #注册
    register_list = []
    register_list.append(reg_user)      #将用户信息加入列表
    register_list.append(reg_pwd)
    register_list.append(reg_email)
    register_list.append(reg_phone)
    register_list.append('1')
    with open('regist', 'a', encoding='utf-8') as f:   #将用户信息写入文件
        li = '|'.join(register_list)
        f.write(li + '\n')

    print("注册/添加信息:", li)




def delete_func(dele_user, type_user):       #删除普通用户
    if type_user == '1':          #若删除的是普通用户
        exit_flag = False
        with open('regist', 'r+', encoding='utf-8') as f1, open('regist_new', 'w', encoding='utf-8') as f2:
            for line in f1:
                ret_list = line.strip().split('|')
                if ret_list[0] == dele_user:
                    exit_flag = True        #标志位原本设为False，当找到相应用户删除后，标志位设为True
                    print("普通用户删除成功")
                    continue
                f2.write(line)
        shutil.move('regist', 'regist_bak')
        os.rename('regist_new', 'regist')

        if not exit_flag:
            print("要删除普通用户不存在")
    elif type_user == '2':      #若删除的是管理员用户
        print("没有权限删除管理员帐号")



def upper_level(upper_user):    #升级为管理员
    with open('regist', 'r+', encoding='utf-8') as f1, open('regist_new', 'w', encoding='utf-8') as f2:
        for line in f1:
            li = line.strip().split('|')
            if li[0] == upper_user:
                li[-1] = '2'
                print("%s已成为管理员" % upper_user)
                f2.write('|'.join(li) + '\n')
                continue
            f2.write(line)

    shutil.move('regist', 'regist_bak')
    os.rename('regist_new', 'regist')



def search(search_info):     #简单搜索
    with open('regist', 'r+', encoding='utf-8') as f:
        for line in f:
            ret_list = line.strip().split('|')
            if search_info in ret_list:
                print(ret_list)



def get_usertype(user):     #通地用户名获得用户类型，返回1或2
    with open('regist', 'r+', encoding='utf-8') as f:
        for line in f:
            li = line.strip().split('|')
            if li[0] == user:
                return li[-1]      #返回帐号的类型  1或2



@outer1
def admin_user():            #管理员调用
    num = input("请选择:1.修改密码;2.查看本用户信息;3.修改普通用户密码;"
                                      "4.删除/添加普通用户;5.权限管理;6.关键字搜索普通用户信息;7.退出:")
    if num == '1':
        new_pwd = input("请输入新的密码:")
        change_pwd(new_pwd)
    elif num == '2':
        look_information()
    elif num == '3':
        user_changed = input("请输入修改密码的用户名:")
        type_user = get_usertype(user_changed)
        new_pwd = input("请输入新的密码:")
        change_pwd(user_changed, new_pwd, type_user)
    elif num == '4':
        add_or_dele = input("1.删除普通用户;2.添加普通用户")
        if add_or_dele == '1':
            delete_username = input("请输入要删除普通用户的用户名:")
            type_user = get_usertype(delete_username)
            delete_func(delete_username, type_user)
        elif add_or_dele == '2':
            regi_username = input("请输入注册用户名:")
            regi_pwd = input("请输入注册密码:")
            regi_email = input("请输入邮箱:")
            regi_phone = input("请输入电话:")
            register(regi_username, regi_pwd, regi_email, regi_phone)
    elif num == '5':
        upper_user = input("请输入升级为管理员的普通用户名:")
        upper_level(upper_user)

    elif num == '6':
        search_information = input("请输入要查找的关键字:")
        search(search_information)
    elif num == '7':
        sys.exit()





def main():

    while True:
        choice = input("请选择:1.登陆;2.注册;3.修改密码;4.查看信息;5.后台管理;6.退出:")
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
            print("注册成功".center(50, '*'))
        elif choice == '3':
            new_pwd = input("请输入新的密码:")
            current_user = USER_LOGIN['current_user']
            change_pwd(current_user, new_pwd)
            print("修改密码成功,请重新登陆".center(50, '-'))
            sys.exit()
        elif choice == '4':
            look_information()
        elif choice == '5':
            admin_user()
        elif choice == '6':
            sys.exit()

main()

