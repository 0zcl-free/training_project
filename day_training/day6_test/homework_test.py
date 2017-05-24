import re

# num = input("please input:")
#只算加减
# r = 9+9-6+5-3 #不能把'9+9-6+5-3' 直接通过int() 得出数字
# print(r)

# #先算 8+9
# s = re.split(r'(\D)', num)   #['8', '+', '9']
# print(s)
# #print(s[1])   # +
# if s[1] == '+':
#     add = int(s[0]) + int(s[2])
#     print(add)
# elif s[1] == '-':
#     low = int(s[0]) - int(s[2])
#     print(low)

'''
num = input("please input:")
#再算8+5+6－5
s = re.split(r'(\D)', num)
print(s)

if s[1] == '+':
    result = int(s[0]) + int(s[2])
    print(result)
elif s[1] == '-':
    result = int(s[0]) - int(s[2])
    print(result)

for i in range(3):   #去掉前三个
    s.remove(s[0])

print(s)  #['+', '6', '－', '5']

s.insert(0, str(result))

print(s)  #['13', '+', '6', '－', '5']
#感觉可以用迭代
'''

#8+5+6－5
num = input("please input:")
sa = re.split(r'(\D)', num)


def func(s):

    if s[1] == '+':

        result = int(s[0]) + int(s[2])
    elif s[1] == '-':
        result = int(s[0]) - int(s[2])

    for i in range(3):  # 去掉前三个
        s.remove(s[0])

    s.insert(0, result)   #局部变量引用赋值前的结果
    print(s)

    if len(s) == 1:
        print(result)
    else:
        func(s)

func(sa)