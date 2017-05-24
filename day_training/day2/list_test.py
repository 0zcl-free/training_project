num = [34, 9, 56, 55, 78, 14, 34, 9, 80, 9, 10, 9]
print(num)

count_of = num.count(9)    #9的个数
print("the num of 9:%d" % count_of)

for i in range(num.count(9)):    #根据9的个数决定循环次数
    num[num.index(9)] = 9999      #找到9的位置，改变其值
print(num)

for i in range(num.count(34)):
    num.remove(34)

print(num)