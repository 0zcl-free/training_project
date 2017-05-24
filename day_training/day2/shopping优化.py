
username = input("Username:")
password = input("Password:")
print(username)
print(password)

print("Welcome logging".center(50,'-'))

save_user = open("save_username.txt", "w")  #打开文件
save_user.write(username)                      #将文件用户密码保存
save_user.write(password)



salary = input("Input your salary:")   #输入salary

if salary.isdigit():              #判断salary是否数字
    salary = int(salary)
else:
    print("Invalid data type...please input again.")
    exit()

welcome_msg = "Welcome to Spping Mall".center(50,'-')
print(welcome_msg)          #输出欢迎界面

product_list = [            #商品列表，里面放元组（只读列表）
    ('Ipad',7000),
    ('Iphone',5400),
    ('Book',40),
    ('fruit',14.4),
    ('Car',150000),
    ('Bike',250)
]

shopping_car = []

exit_flag = False
while not exit_flag:
    print("Product list".center(50,'-'))
    for item in enumerate(product_list):    #输出商品列表
        index = item[0]                     #eg:item == (0, ('Ipad', 7000)) 商品序号，从0开始
        prod_name = item[1][0]              #重要
        prod_price = item[1][1]
        print(index,':',prod_name,prod_price)

    user_choice = input("[q=quit,c=check]What do you want to buy?:")
    if user_choice.isdigit():        #输入的是数字，选商品
        user_choice = int(user_choice)
        if 0 <= user_choice < len(product_list):   #输出的数字不超界
            p_item = product_list[user_choice]     #选中的元组，eg:('Ipad',7000)
            count_of_prod = int(input("How many do you want to buy?:"))   #输入购买商品数量
            if p_item[1] * count_of_prod <= salary:                #钱够
                for i in range(count_of_prod):                    #放入购物车
                    shopping_car.append(p_item)
                salary -= p_item[1] * count_of_prod                #扣钱
                print("%s in your Shopping_car;and your current balance is %s" % (p_item ,salary))
            else:
                #余额不足
                print("your balence is %s;and You have no enough money to buy it!" % salary)
        else:
            print("The number go beyond.Try again...")
    else:                  #user_choice == 'q' or 'quit':   这样是错误的！！！
            if user_choice == 'q' or user_choice == 'quit':                #输入q退出
                print('Purchased product as below'.center(50, '*'))
                print(shopping_car)
                print('Your balance is %s' % salary)
                print('End'.center(50,'*'))
                exit_flag = True
            elif user_choice == 'c' or user_choice == 'check':              #输入c检查，输出购物车列表
                print('Purchased product as below'.center(50,'*'))
                for item in shopping_car:
                    print(item)
                print('Your balance is %s' % salary)
            else:
                print("Please input the number of product...")


