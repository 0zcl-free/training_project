


'''
import json
dic = {'k1': 'v1'}
print(dic, type(dic))
#序列化：将python基本数据类型转化成字符串形式
result = json.dumps((dic))
print(result, type(result))
# {'k1': 'v1'} <class 'dict'>
# {"k1": "v1"} <class 'str'>

s1 = '{"k1": 123}'
#反序列化：将字符串形式转化成python基本数据类型
dic = json.loads(s1)
print(dic, type(dic))
#{'k1': 123} <class 'dict'>
'''

'''
import requests
import json

response = requests.get('http://wthrcdn.etouch.cn/weather_mini?city=北京')
response.encoding = 'utf-8'

print(response.text, type(response.text))  #<class 'str'>

dic = json.loads(response.text)     #将字符串格式转化为字典
print(type(dic))
'''


import json
li = [11,22,33,44]
#1.将li 序列化
#2.将序列化后的字符写到文件中
json.dump(li, open('db', 'w'))

#1.从文件读取字符串
#2.将字符串反序列成python基本数据类型
lis = json.load(open('db', 'r'))
print(lis, type(lis))

'''
h3
{
color:#fff;
background-color:#008eb7;
-moz-border-radius: 3px;
border-radius: 3px;
padding:3px;
margin:10px 0px;
text-shadow:2px 2px 3px #404040;
}
'''