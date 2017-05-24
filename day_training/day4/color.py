
def outer(func):
    def inner(*args, **kwargs):
        print('before')
        r = func(*args, **kwargs)
        print('after')
        return r
    return inner
#@ + 函数名
#功能：
#       1.自动执行outer函数，并且将其下面的函数f1当作参数传递
#       2.将outer函数的返回值，重新赋值给f1
@outer
def f1(args, args2, args3):
    print(args, args2, args3)
    return 'fffff'

ret = f1('aaa', 'bbb', 'ccc')
print(ret)