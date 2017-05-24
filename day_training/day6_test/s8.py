
import re   #正则表达式本身就是小型编程语言

"""
#findout  把匹配结果通过列表返回

r =re.findall('zcl', 'fzclfjfrijzclfeizcfj')
print(r)  #['zcl', 'zcl']


# . 匹配到除换行符以外的任一个字符
r1 =re.findall('z.l', 'fzolfjfrijzclfeizcfj')
print(r1)    #['zol', 'zcl']
r1 =re.findall('z.l', 'fz\nlfjfrijzclfeizcfj')
print(r1)    #['zcl']


# ^ (shift+6)区配到以 xx字符开头
r2 =re.findall('^z.l', 'fz\nlfjfrijzclfeizcfj')
print(r2)   #[]
r3 =re.findall('^z.l', 'zcllfz\nlfjfrijzclfeizcfj')
print(r3)   #['zcl']
"""

"""
# $  匹配到以xx结束的字符
r4 =re.findall('z.l$', 'zcllfz\nlfjfrijzclfeizcfj')
print(r4)      #[]
r5 =re.findall('z.l$', 'zcllfz\nlfjfrijzclfeizcfjzcl')
print(r5)     #['zcl']
"""

"""
# *  区配*前面的字符0到多次
# +  重复一次或更多次
r6 =re.findall('z.*l', 'zcgfchthllfz\nlfjfrijzclfeizcfjzcl')
print(r6)     #['zcgfchthll', 'zclfeizcfjzcl']

r7 =re.findall('z.+l', 'zcgfchthfz\nlfjfrijzcfeizcfjzc')
print(r7)     #[]

# {n}	重复n次
# {n,m}	重复n到m次
# {n,}	重复n次或更多次



# [bc]  匹配b或c

"""
# r9 = re.findall('a[bd]c', 'dfjabdcdjfabcdf')
# print(r9)
# r8 = re.findall('zc{3}l', 'zccclgfchthfz\nlfjfrijzcfeizcfjzc')
# print(r8)       #['zcccl']
"""
#[a-z] 匹配a至z任意一个
r9 = re.findall('a[a-z]c', 'dfjabdcdjfatcdf')
print(r9)      #['atc']


#[] 里面仍有功能有三个：  [a-z]   [\d]区配数字  [^] 非
r10 = re.findall('a[^f]d', "afd")
print(r10)     #[]
r11 = re.findall('a[^f]d', "ard")
print(r11)    #['ard']
r12 = re.findall(r'a\df', "a8f")
print(r12)   #['a8f']
"""
