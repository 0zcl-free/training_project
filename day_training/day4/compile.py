"""
s = "print(123)"
#编译：把字符串编译成代码  single, eval, exec三种模式
r = compile(s, "<string>", "exec")

print(r)
exec(r)    #执行代码
"""


'''
#exec 只执行表达式但没有返回值
re = exec("7+8")
print(re)
#eval 有返回值 ，执行表达式，并获取结果
ret = eval("8+9")
print(ret)
'''


#快速查看，对象提供了哪些功能
# print(dir(list))
# help(list)


"""
# #元组
r = divmod(94,10)
print(r)
#
# print(r[0])
# print(r[1])

n1, n2 = divmod(99,10)
print(n1)
"""

'''
s = 'zcl'
#判断s 是否 str的实例
r = isinstance(s, str)
r1 = isinstance(s, list)
print(r)
print(r1)
'''

'''
def f1(arg):
    if arg > 22:
        return True    #若返回True,则接收

li = [11,22,23,33,44]
ret = filter(f1, li)
print(list(ret))
'''


'''
f1 = lambda a: a > 30

ret = f1(40)
print(ret)


li = [11,22,33,44,55]

result = filter(lambda a: a > 33, li)
print(list(result))
'''


'''
#功能：列表每个元素+ 100
li = [11,22,33,44,55]

def f1(args):
    lis =[]
    for i in args:
        lis.append(100 + i)

    return lis


result = f1(li)
print(result)
'''

#map(函数，可迭代的对象)  可统一进行操作
# li = [11,22,33,44,55]
# ret = map(lambda a: a + 100, li)
# print(list(ret))


'''
NAME = 'ALEX'

def show():
    a = 123
    b = 'zcl'
    print(locals())     #打印所有局部变量
    print(globals())    #打印所有全局变量（包括python提供的全局变量）

show()
'''

# s = 'h'
# dict = {s : 1}
# print(hash(s))  #生成哈希值
# print(id(s))
# print(len(s))



s1 = '程亮'

print(len(s1))   #python3 传字符长度
b = bytes(s1, encoding='utf-8')
print(len(b))    #也可转化为字节，再传字节长度

