import gevent


def func1():
    print('\033[31;1mAAAA...\033[0m')
    gevent.sleep(2)
    print('\033[31;1mBBBB...\033[0m')


def func2():
    print('\033[32;1mCCCC...\033[0m')
    gevent.sleep(1)
    print('\033[32;1mDDDD...\033[0m')


def func3():
    print("\033[33;1mEEEE...\033[0m")
    gevent.sleep(0)
    print("\033[33;1mFFFF...\033[0m")

gevent.joinall([
    gevent.spawn(func1),
    gevent.spawn(func2),     #spawn:生产
    gevent.spawn(func3),
])