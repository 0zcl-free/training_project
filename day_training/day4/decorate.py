
def f1():
    print('123')


def f2(a):
    a()

f2(f1)   #函数整体可作为参数传递！