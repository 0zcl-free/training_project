'''
r = min([11,22,33])
print(r)


r1 = pow(2, 10)
print(r1)

li = [11,22,33,44]
li.reverse()     #翻转
print(li)
'''

# r = round(1.9)    #四舍五入
# print(r)


l1 = ['zcl',11,33,44]
l2 = ['is',55,66]
l3 = ['good',99,88]

# s = l1[0] + l2[0] + l3[0]
# print(s)

r = zip(l1, l2, l3)
#print(list(r))
temp = list(r)[0]
ret = ' '.join(temp)
print(ret)

