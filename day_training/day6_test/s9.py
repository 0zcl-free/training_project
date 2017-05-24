import re

# re.match('com', 'comwww.runcomoob')
# re.search('\dcom', 'www.4comrunoob.5com')
# 一旦匹配成功，就返回一个match object 对象，对象拥有下列方法；
# group() 返回被re 匹配的字符串
# start()  返回匹配开始的位置
# end()    返回匹配结束的位置
# span()   返回一个元组包含匹配（开始，结束）的位置



#s = re.match('com', 'www.runcoomoob')#只匹配起始位置

# 否则曝错
# Traceback (most recent call last):
#   File "C:/Users/Administrator/PycharmProjects/laonanhai/day6_test/s9.py", line 15, in <module>
#     print(s.span())   #注意位置，不是0－3
# AttributeError: 'NoneType' object has no attribute 'span'

# print(s)    #<_sre.SRE_Match object; span=(0, 3), match='com'>
# print(s.span())   #注意位置，不是0－3
# s1 = re.match('coom', 'mwww.runcoomoob')
# print(s1)   #None


# s2 = re.search('com', 'www.runcomoocomb')
# print(s2)
# #<_sre.SRE_Match object; span=(7, 10), match='com'>  注意前面的找到则不再往后找

"""
#sub subn 替换  re.sub(pattern, repl, string, max)   max 最大替换次数
s3 = re.sub("g.t", "have", "I get A, I got B, I gut C", 2)
print(s3)    #I have A, I have B, I gut C

s4 = re.subn("g.t", "have", "I get A, I got B, I gut C")
print(s4)    #('I have A, I have B, I gut C', 2)   多了替换次数
"""


"""
#re.split()  分割
s5 = re.split('\d+', 'one1two2three3four4')
print(s5)   #['one', 'two', 'three', 'four', '']


#把那些经常使用的正则表达式编译成正则表达式对象，可以提高一定的效率！
text = 'JGood is a handsome boy, he is cool, clever, and so on...'
regex = re.compile(r'\w*oo\w*')   #regex 是对象
print(regex.findall(text))   #['JGood', 'cool']
"""
"""
r6 = re.search('\\com', 'www.run\comoob')
print(r6.group())   #只匹配到'com'    为什么
print(r6)


#f = open("c:\abc.txt")   #错误f = open("c:\\abc.txt")
r7 = re.search(r'\\com', 'www.run\comoob')   #匹配到'\com'  翻译到屏幕是'\\com'
print(r7)
"""


# r8 = re.search('\com', 'www.run\comoob')
# print(r8)           #只匹配到'com';若要匹配到'\com'  re.search('\\\\com', 'www.run\comoob')

# r9 = re.search('\\\\', 'www.run\comoob')
# print(r9)       #匹配到‘\’   '\\\\'  python  将其翻译为'\\'  re 模块将其编译为'\'

r10 = re.search(r'\\com', 'www.run\comoob')   #加r , 表示python 不翻译，re 翻译
print(r10)



