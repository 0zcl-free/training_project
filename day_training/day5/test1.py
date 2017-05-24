"""
s1 = 'zcl %'
print(s1)

#当格式化时,字符串中出现点位符%s, 需要用%%输出%
s2 = 'zcl %s %%' % ('good')
print(s2)

s3 = 'zcl %s %' % ('good')
print(s3)
"""

"""
li = [11,22,33,44]
result = filter(lambda a:a > 22, li)
print(result)   #具有生成指定条件数据能力的一个对象
print(list(result))
"""

"""
def func():
    print('start')
    yield 1
    yield 2
    yield 3

func()    #运行后，竟然没有输出

"""

"""
#若在普通函数中出现yield 则称为生成器
def func():
    print('start')
    yield 1
    yield 2
    yield 3

ret = func()
print(ret)    #<generator object func at 0x0000000003020438>
"""

"""
def func():
    print('start')
    yield 1
    yield 2
    yield 3

ret = func()     #没有执行函数
for i in ret:   #每次循环执行一个yield
    print(i)

# 输出
# start
# 1
# 2
# 3
"""


def myrange(arg):
    start = 0
    while True:
        if start > arg:
            return
        yield start
        start += 1

ret = myrange(3)
r = ret.__next__()
print(r)
r = ret.__next__()
print(r)
r = ret.__next__()
print(r)
r = ret.__next__()
print(r)
r = ret.__next__()
print(r)