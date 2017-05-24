'''
def f1(a1,a2):
    return a1 + a2

def f1(a1,a2):
    return a1 * a2

retu = f1(8, 8)
print(retu)
'''

'''
#函数参数传递时，传引用还是再传一份值？
def f1(a1):
    a1.append(999)

li = [11,22,33,44]
f1(li)
print(li)
'''


num = [11,22,33]
def f1():
    print(num)
    num.append(44)
   # num = [44,55,66]   #对全局变量 列表进行重新赋值
    print(num)       #全局变量num可修改


f1()
