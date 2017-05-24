
diction = {
    123:'zcl',
    456:{'name':'Alex Li'},
    789:{'name':'ZCL',
         'age':21,
         'addre':'huilai'},
    890:'qwe'
}

print(diction)   #输出整个字典

"""
print(diction[123])    #输出字典的元素
print(diction[789])

diction[789]['name'] = 'Boss ZCL'   #修改字典元素
diction[789]['love'] = 'My family'  #没有的话将自动添加
del diction[123]
#del diction
print(diction[789])
print(diction)
"""


"""
v = diction.get(123)
print(v)                  #通过key,输出value
v1 = diction.get(888)
print(v1)                 #若key不存在，输出None,注意不会曝错

print(diction.keys())      #打印KEY
print(diction.values())    #打印VALUE

print(123 in diction)     #判断KEY是否在字典
"""

#print(diction.setdefault(1234, 'parent'))   #取一个KEY，若不存在，则输出None

#{56: 'zcl', 1: 'zcl', 2: 'zcl', 3: 'zcl', 4: 'zcl'}
#print(diction.fromkeys([1,2,3,4,56],'zcl'))   #不建议用
print(diction.items())
#dict_items([(456, {'name': 'Alex Li'}), (890, 'qwe'), (123, 'zcl'), (789, {'age': 21, 'addre': 'huilai', 'name': 'ZCL'})])


#循环字典
"""
print("------------------")
for k,v in diction.items():    #效率低！因为要有一个dict to list的转换过程
    print(k,v)
"""

for key in diction:             #效率高！
    print(key,diction[key])