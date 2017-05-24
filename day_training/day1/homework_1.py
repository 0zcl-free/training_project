username = "zcl"      #设置正确的用户名与密码
password = 123
count = 0
lockuser_open = open("lock_username.txt", "r")    #打开文件
str = lockuser_open.read()         #将已锁定的用户名读入

for i in range(10):
    if count < 3:
        usern = input("Username:")   #输入用户名
        passwd = input("Password:")  #输入密码
        if usern == username and password == passwd:  #两者都正确
            print("Welcome logging...")
            count = 0     #将count置为0
            break
        elif usern == str:   #若输入用户名是已锁定的用户名
            print("Your username have been locking...")
            break
        else:              #若输错，但输入的不是已锁定的
            print("Logging false...")
            count += 1      #输错次数+1
            if count >= 3:
                print("Locking...")
                lock_user = open("lock_username.txt","w")      #将输错3次的用户名保存到硬盘
                lock_user.write(usern)
                break

