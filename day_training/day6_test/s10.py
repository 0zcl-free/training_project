
import re

#正则分组：去已经匹配到的数据中再匹配数据
"""
# 无分组
origin = "has fkdghggfhh"
r = re.match("h\w+", origin)
print(r.group())  # 获取匹配到的所有结果
print(r.groups())  # 获取模型中匹配到的分组结果
print(r.groupdict())  # 获取模型中匹配到的分组结果

# has
# ()
# {}
"""


"""
# search()  分组也一样，只是找的方式不同
origin = "has fkdghggfhh"
r = re.match("h(?P<name>\w+)", origin)
print(r.group())  # 获取匹配到的所有结果
print(r.groups())  # 获取模型中匹配到的分组结果
print(r.groupdict())  # 获取模型中匹配到的分组中所有执行了key的组

# has
# ('as',)
# {'name': 'as'}
"""



origin = "hasbbcc fkdghggbbccfhhbbcc halbbcc"
#r = re.findall("(h\w+)", origin)    #无用分组   ['has', 'hggfhh', 'hal']
#r = re.findall("h(\w+)", origin)    #只拿分组里面的东西  ['as', 'ggfhh', 'al']
#r = re.findall("h(\w+)bbc", origin)  #['as', 'ggbbcfhh', 'al']
r = re.findall("h(\w+)b(bc)c", origin)
print(r)    #[('as', 'bc'), ('ggbbccfhh', 'bc'), ('al', 'bc')]
"""
# # 有分组
# origin = "hello alex bcd abcd lge acd 19"
# r = re.findall("a((\w*)c)(d)", origin)
# print(r)
"""

"""
# 无分组
origin = "hello alex bcd alex lge alex acd 19"
r = re.split("alex", origin,1)
print(r)        #['hello ', ' bcd alex lge alex acd 19']

# 有分组
origin = "hello alex bcd alex lge alex acd 19"
r1 = re.split("(alex)", origin, 1)
print(r1)   #['hello ', 'alex', ' bcd alex lge alex acd 19']
r2 = re.split("al(ex)", origin, 1)   #重要
print(r2)   #['hello ', 'ex', ' bcd alex lge alex acd 19']
"""

