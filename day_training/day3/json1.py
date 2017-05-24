import json

s = "[11,22,33,44]"
s1 = '["zcl",12]'   #内部字符串必须是双引号，单引号曝错！
s2 = '(11,22)'
n = json.loads(s)
print(n)
#将一个字符串，转换成python的基本数据类型[]，{}可以，（）不行
n1 = json.loads(s1)
print(n1)
n2 = json.loads(s2)  #出错！
print(n2)