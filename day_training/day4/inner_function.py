#callable()   判断函数能否被执行
'''
def f1():
    pass

f2 = 123

print(callable(f1))
print(callable(f2))
'''

'''
r = chr(65)      #把数字转化为字母
print(r)

n = ord('a')     #把字母转化为数字
print(n)
'''


"""
li = ['c','b','a']
result = ''.join(li)
print(result,type(result))
"""


'''
import random
li = []
for i in range(6):
    temp = random.randrange(65, 91)  #产生65<=   <91的随机整机
    c = chr(temp)              #将数字转化为字母
    li.append(c)               #将字母加入列表
# li = ['c', 'b', 'a']  -> cba
result = ''.join(li)
print(result)
'''


'''
import random
li = []
for i in range(6):
    if i == 2 or i == 4:      #第三位和第五位产生数字
        num = random.randrange(0, 10)  # 产生0-9的随机整机
        li.append(str(num))            #将数字转化为字符，否则join方法曝错
    else:
        temp = random.randrange(65, 91)
        c = chr(temp)              #将数字转化为字母
        li.append(c)               #将字母加入列表
# li = ['c', 'b', 'a']  -> cba
result = ''.join(li)
print(result)
'''



import random
li = []
for i in range(6):
    r = random.randrange(0, 5)      #产生随机数0－4
    if r == 2 or r == 4:      #当产生的随机数为2或4时，则产生数字，否则产生字母
        num = random.randrange(0, 10)  # 产生0-9的随机整机
        li.append(str(num))            #将数字转化为字符，否则join方法曝错
    else:
        temp = random.randrange(65, 91)
        c = chr(temp)              #将数字转化为字母
        li.append(c)               #将字母加入列表
# li = ['c', 'b', 'a']  -> cba
result = ''.join(li)
print(result)