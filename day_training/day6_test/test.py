# obj = __import__("lib.manager")
# print(obj)  #没有导入manager.py
# #<module 'lib' from 'C:\\Users\\Administrator\\PycharmProjects\\laonanhai\\day6_test\\lib\\__init__.py'>
# obj.order()     #AttributeError: 'module' object has no attribute 'order'
#
# obj1 = __import__("lib.manager", fromlist=True)   #表示按路径连接方式导入
# print(obj1)   #导入manager
# #<module 'lib.manager' from 'C:\\Users\\Administrator\\PycharmProjects\\laonanhai\\day6_test\\lib\\manager.py'>
# obj1.order()


"""
请选择：1.加减;2.乘除2
please input:50*2/3
33.333333333333336
"""


import re

#计算加减
def add_substract(s):
    result = 0
    if s[1] == '+':
        result = int(s[0]) + int(s[2])
    elif s[1] == '-':
        result = int(s[0]) - int(s[2])

    for i in range(3):  # 去掉前三个
        s.remove(s[0])

    s.insert(0, result)   #局部变量引用赋值前的结果

    if len(s) == 1:
        print(result)
    else:
        add_substract(s)


#计算乘除  8*9/5
#计算加减
def mul_mov(s):
    result = 0
    if s[1] == '*':
        result = int(s[0]) * int(s[2])
    elif s[1] == '/':
        result = float(s[0]) / int(s[2])
        result = int(result)

    for i in range(3):  # 去掉前三个
        s.remove(s[0])

    s.insert(0, result)   #局部变量引用赋值前的结果

    if len(s) == 1:
        print(result)
    else:
        mul_mov(s)


def main():
    choose = input("请选择：1.加减;2.乘除")
    num = input("please input:")
    if choose == '1':
        sa = re.split(r'(\D)', num)
        add_substract(sa)
    elif choose == '2':
        sa = re.split(r'(\D)', num)
        mul_mov(sa)


if __name__=="__main__":
    main()