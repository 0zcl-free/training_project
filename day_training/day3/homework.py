

print("1.获取ha记录")
print("2.增加ha记录")
print("3.删除ha记录")




def gain():
    read = input("请输入backend:")
    f = open('work', 'r+', encoding='utf-8')
    for line in f:
        read_str = f.readline()
        if read_str == 'backend ' + read + '\n':
            print(f.readline())
        elif read_str == False:
            continue


flag = True
while flag == True:

    input_str = input("用户输入:")
    if input_str == '1':
        gain()         #记录获取


