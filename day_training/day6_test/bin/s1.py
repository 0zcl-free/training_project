



#print(vars(s2))   #获取s2的变量

# r = s2.abs(-4)
# print(r)


# 全局变量
# __doc__      #获取文件注释
# __file__
# __cached__
# __name__
# __package__

"""
这是注释
"""


#print(__doc__)      #无注释输出None

import sys
import os

"""
print(__file__)   #获取当前.py运行文件的路径
#C:/Users/Administrator/PycharmProjects/aonanhai/day6_test/s1.py
print(os.path.abspath(__file__))  #攻取文件绝对路径
#C:\\Users\Administrator\PycharmProjects\laonanhai\day6_test\s1.py
#os.path.dirname()#找到某文件的上级目录
ret = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(ret)
print(ret)

import s2
"""


