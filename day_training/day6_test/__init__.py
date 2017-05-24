

def func(num):
    if num == 1:
        return 1
    else:
        return num * func(num - 1)

result = func(7)
print(result)
