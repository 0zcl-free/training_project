import sys
import time


def view_bar(num, total):
    rate = num / total
    rate_num = int(rate * 100)
    r = '\r%s%d%%' % ("|" * num, rate_num)   # \r 表示重新回到当前行的首行署
    sys.stdout.write(r)          #输出没有换行符
    sys.stdout.flush()           #清空缓存


if __name__ == '__main__':
    for i in range(0, 101):
        time.sleep(0.1)
        view_bar(i, 100)

