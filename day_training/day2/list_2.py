name = ['ZCL', 'Alex', 'Rain', 55, 8, 62, 123, 10, 10, 55, 55, 46, 'ZCL', 'zcl']

print(55 in name)
print('zcl' in name)  #判断列表是否存在一个元素
print(name)

if 55 in name:
    num_of = name.count(55)
    #print("_%d_  55 is or are in name" % num_of)  #打印出个数
    position_of = name.index(55)          #第一个55的位置
    name[position_of] = 555

    print(name)

#将55全改为555
for i in range(name.count(55)):
    position = name.index(55)
    name[position] = 555

print(name)


name2 = [123, 'qwe', 'asd', 555]    #列表元素可重复
name.extend(name2)     #扩展列表
print(name)
print(name2)         #被合并列表仍存在


name.reverse()   #反转列表，注意括号内无参数
print(name)

#name.sort()
#print(name)
print(name2)
name2.pop(1)  #删除指定元素，默认删最后一个
print(name2)


name3 = name2.copy()    #复制
print(name3)