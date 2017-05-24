"""
username = 'ZCL'
user = input("Username:")
if username == user.strip():    #输入若有空格可以忽略   strip girl
    print("Welcome logging...")
else:
    print("False")
"""


'''
name = "zcl,alex,cjy,45"
name2= name.split(",")      #将字符串按，折开，变成列表
print(name2)
print("|".join(name2))      #将列表合并
'''

'''
name = "cheng liang"
print(" " in name)              #判断字符串内有无空格
'''

'''
msg = "Hello, {name}, it's a {good} day"
msg2 = msg.format(name = "ZCL", good = 33)
print(msg2)                 #format:格式化

msg3 = "hahaha{0},ddddd{1}"
print(msg3.format("Alex", 33))

#Hello, ZCL, it's a 33 day
#hahahaAlex,ddddd33
'''


'''
name = 'chengliang zhang'
print(name[2:6])
print(name.find('e'))     #找到则返回索引
print(name.find('ang'))
print(name.find('asd'))
print(name.find('3'))     #找不到则返回－1
'''

'''
name = 'zcl'
print(name.isalnum())   #不能包括特殊字符False，阿拉伯数字可以True
print(name.endwith('l')
'''