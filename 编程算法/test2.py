
a = None
if not a:
    print("aaa")
else:
    print("BB")

print(5//2)
# 但是，预计在Python3.0发布时，就没有这种折中情况了，，" / "就一定表示 浮点数除法，返回浮点结果;" // "表示整数除法。

li = [1,22,33,44,55,66]

for i in range(8, 0, -1):
    print(">>", i)

# >> 8
# >> 7
# >> 6
# >> 5
# >> 4
# >> 3
# >> 2
# >> 1


# arr[0], arr[end] = arr[end], arr[0]
aa = 11
bb = 22
print("aa, bb:", aa,bb)
aa, bb = bb, aa
print("aa,bb:", aa,bb)

