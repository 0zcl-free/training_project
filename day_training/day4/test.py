'''
import color

color.f1()
'''
#
# f = open('test', 'r+', encoding='utf-8')
# for line in f:
#     if line.startswith("123"):
#         r = line.replace("refg", "aaaa")
#         line = r
#         f.write(r)
#         print(r)
#     else:
#         print("?")
#
#
# li = [11,22,333]
# li[-1] = 44
# print(li)
# print(li[-1])

print("AA")
with open('test', 'r', encoding='utf-8') as f:
    for line in f:
        if line.startswith("123"):
            print("As")
            li = line.replace("123", "666")
            print(li)