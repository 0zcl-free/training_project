
# li = [2,3,6,8]
# li2 = [5,6,4]
# print list(set(li+li2))

def func(x):

    count = 0
    while(x):

        count += 1
        x = x&(x-1)

    return count


ret = func(2015)
print ret