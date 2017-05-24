
modu = __import__("lib.aa")   #只是导入lib
print(modu)
#<module 'lib' from 'C:\\Users\\Administrator\\
# PycharmProjects\\laonanhai\\day9\\lib\\__init__.py'>
obj_name = modu.aa.C().name
print(obj_name)


# lib = __import__("lib.aa")  #解释器内部用的，官方不建议用
# lib.aa

#
# import importlib
# aa = importlib.import_module("lib.aa")  #导入lib.aa 官方建议
# print(aa.C().name)