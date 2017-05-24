#set 无序，不重复序列

#1.创建集合

"""
li = []
list()        #里面可循环的参数，eg:  元组，字符串
#原理：通过执行list __init__,内部执行for循环(11,12,3)变成[11,12,3]
lis = list((11,12,3))
print(lis)
"""


#dic = {123:'qwe'}

"""
s = {123,4,123}     #1.创建集合
s1 = set()          #2.创建空集合
s2 = set([11,12,34,56,56])       #3.创建空集合,里面是可循环的参数

print(s)
print(s1)
print(s2)
print(type(s))
"""

#2.功能
s1 = {14,15,99}
s3 = {15,14,7}
#s1.add(16)               #添加集合元素{16, 13, 14, 15}

#s1.discard(33)           #删除集合指定元素，若没有相应元素，不报错！！ 最优
#s1.clear()               #删除集合所有元素
#s1.remove(14)            #删除集合指定元素，若没有相应元素，则报错

#s2 = s1.copy()           #复制
#print(s2)                #{13, 14, 15}

#s2 = s1.difference(s3)       #{13}，输出s1中与s3不同的元素
#s1.difference_update(s3)     #s1更新成s1有,s2没有的元素
#print(s1)

#s2 = s1.intersection(s3)     #s1与s3相同的元素
#s1.intersection_update(s3)   #s1更新成 s1与s3相同的元素
#print(s1)

#s2 = s1.isdisjoint(s3)      #Return True if two sets have a null intersection
#print(s2)                   #判断是否有相同元素

#s2 = s1.issubset(s3)        #判断s1是否是s3的子集
#print(s2)
#s2 = s1.issuperset(s3)      #判断s1是否是s3的父集

#s2 = s1.symmetric_difference(s3)      #取s1,s3的交集
#s1.symmetric_difference_update(s3)    #更新s1  成s1,s3的交集

#s2 = s1.union(s3)                     #取s1与s3的并集

'''
s1.update(s3)            #更新s1，将s3元素加入,可以接收一个可迭代的对象
s1.update([1,2,3])
s1.update('zcl')
print(s1)
'''

'''
s2 = s1.pop()                #s1随机移除一个,拿到移除的值s2
print(s1)
print(s2)
'''
