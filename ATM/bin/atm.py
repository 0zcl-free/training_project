
"""
ATM程序的执行文件
"""
import os
import sys

dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   #找到路径
sys.path.insert(0, dir)     #添加路径
print(dir)

#将main.py里面所有代码封装成main变量
from core import main

if __name__ == "__main__":
    #这里我刚开始用run()就爆错了
    main.run()
