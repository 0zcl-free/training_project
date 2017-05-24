# 1，打开文件

'''
#只读
f = open('db', 'r')
# 只写，之前选清空
f = open('db', 'w')
# 文件存在，报错；不存在，创建并只写
f = open('db', 'x')
# 追加
f = open('db', 'a')
'''


'''
f = open('db','rb')    #读二进制
data = f.read()
print(data,type(data))
f.close()
# b'zcl|123\r\nqwe|123\r\n123|qwe' <class 'bytes'>
'''


"""
f = open('db','ab')
# f.write('hello')     #以二进制写，否则错误
#TypeError: 'str' does not support the buffer interface

f.write(bytes('hello',encoding='utf-8'))   #写字节
f.close()
"""


'''
f = open('db', 'r+', encoding='utf-8')

data = f.read(1)

print(f.tell())
#z666123       会覆盖！
#qwe|123
# r+ 模式下，seek(1)指在1个字节后，注意：是字节位置
f.seek(f.tell())   #主动把针指调至某位置
f.write('777')
f.close()
'''


'''
f = open('db','r+',encoding='utf-8')
data = f.read(2)
print(data)
'''

'''
f = open('test','w')    #已经先被清空
print(f.readable())
'''


'''
f = open('db', 'r', encoding='utf-8')
data_line = f.readline()
data_line2 = f.readline()
print(data_line)
'''

'''
f = open('db', 'r+', encoding='utf-8')
f.seek(5)
f.truncate()
f.close()
'''

'''
f = open('db', 'r+', encoding='utf-8')
for line in f:
    print(line)
'''

'''
#把db文件复制到db1中去
with open('db', 'r', encoding='utf-8') as f1,open('db1', 'w', encoding='utf-8') as f2:
    for line in f1:
        f2.write(line)
'''

'''
#把db文件前10行复制到db1中去
with open('db', 'r', encoding='utf-8') as f1,open('db1', 'w', encoding='utf-8') as f2:
    times = 0
    for line in f1:
        times += 1
        if times <= 10:
            f2.write(line)
        else:
            break
'''


#把db文件复制到db1中,并将db1的alex改为zcl
with open('db', 'r', encoding='utf-8') as f1,open('db1', 'w', encoding='utf-8') as f2:
    times = 0
    for line in f1:
        new_str = line.replace('alex', 'zcl')
        f2.write(new_str)