

# import sys
# print(sys.argv)
#
# import diaoyong
# diaoyong.f()
#sys.path.append("D:\\")   #添加路径
#import order

import sys
for intem in sys.path:
    print(intem)
#输出：（优先级从上往下）
# C:\Users\Administrator\PycharmProjects\laonanhai\day5   当前执行脚本目录
# C:\Python34\lib\site-packages\pip-8.1.2-py3.4.egg
# C:\Users\Administrator\PycharmProjects\laonanhai   忽略，只有在pycharm环境下才有
# C:\Windows\SYSTEM32\python34.zip
# C:\Python34\DLLs
# C:\Python34\lib
# C:\Python34
# C:\Python34\lib\site-packages        第三方模块





#模块名称重要性：自己创建的模块不能和python自带模块名称相同，
# 否则在导入内置模块时，会导入自己创建的模块而不是内置模块