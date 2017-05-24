'''
def f():
    pass
r = f()
print(r)
'''
'''
def send(xxoo, content, xx='OK'):     #默认参数
    print(xxoo, content, xx)
    return True

send('zcl','rich')                 #zcl rich OK
('zcl','pool','SB')           #zcl pool SB
'''

'''
def send1(xxoo,  xx='OK',content):     #默认参数
    print(xxoo, xx, content)
    return True

send1('zcl','rich','h')                 #zcl rich OK
'''


'''
#*,可以接收N个实际参数，将实际参数统一放入元组
def f1(*args):
    print(args)

li = [12,'zcl',44,'alex']

f1(li)     #([12, 'zcl', 44, 'alex'],)  列表整体当成一个元素
f1(*li)    #带*，则将列表里面循环，将每一个元素转化到元组元素
'''

'''
#**,自动放入字典,需要有key:value
def f1(**kwargs):
    print(kwargs,type(kwargs))

# f1(n = 'zcl')     #相当与指定参数
# f1(n = 21)

dic = {'k1':'v1','k2':'v2'}
f1(kk = dic)
f1(**dic)        #带**，则将dic里面循环，将每一个元素转化到字典元素
                 #即将dic元素传到字典
'''


'''
#万能参数 *args,**kwargs
def f1(*args, **kwargs):
    print(args)
    print(kwargs)

f1(11,22,33,'zcl',k1 = 'v1',k2 = 'v2')    #自动的
'''

# str.format()
#1. %s,%d
#2. str.format 格式化输出
#以上是python的两种格式化输出

s1 = 'I am [0],age [1]'.format('zcl',21)
print('s1=%s' % s1)
s2 = 'I am {0},age {1}'.format('zcl',21)   #{0}是占位符
print('s2=%s' % s2)
s3 = 'I am {0},age {1}'.format(*['zcl',21])   #加*，与前者相同
print('s3=%s' % s3)

#python规定，若{}里面有name,则后面必须写name = ''
s4 = 'I am {name}, age {age}'.format(name='zcl', age = 21)
print('s4=%s' % s4)
dic = {'name':'zcl', 'age': 21}
s5 = 'I am {name}, age {age}'.format(**dic)
print('s5=%s' % s5)


