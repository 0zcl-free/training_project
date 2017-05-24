
import importlib

aa = importlib.import_module("lib.aa")
obj = aa.C()

assert type(obj.name) is list    #断言
#作用：如果后面的程序很重要，在执行重要程序前断言检查
#比如：银行转账前，进行断言操作
print("dddd...")