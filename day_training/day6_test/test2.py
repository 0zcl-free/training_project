
s = ["12","pp"]
print(s[0].isnumeric())  #True
s1 = ["pp","12"]
print(s1[0].isnumeric())  #False

s2 = '1'
s3 = '2'
s4 = s2 + s3
print(s4)


s5 = "eret67y"
s6 = s5[3:6]
print(s6)


import re
s7 = "5*4-2+((45/3-10*2)-2)"
sa = re.split(r'(\D)', s7)
print(sa)
#['5', '*', '4', '-', '2', '+', '', '(', '', '(', '45', '/', '3', '-', '10', '*', '2', ')', '', '-', '2', ')', '']
while True:
    if "" in sa:
      sa.remove("")       #去掉""
    else:
        break
print(sa)

i =7
for m in range(i, -1, -1):
    print(m)
# 7
# 6
# 5
# 4
# 3
# 2
# 1
# 0

s8 = "(2+(1+(4+5)+9)*2)"
s81= "(594)"


s9 = re.split("\((\d+\))",s81)
print(s9)             #获取括号内数字
#['', '594', '']
data = re.split(r'\(([^()]+)\)', s8)  #我觉得，（）在这里是有特殊意义的，代表分组，要单纯表示括号，就得加转义字符
print(data)    #['(2+(1+', '4+5', '+9)*2)']


s10 = "abdcdeff"
s11 = re.search("[^cd]+", s10)   #天呐！不是非c或d,而是非c且非d
print(s11)     #<_sre.SRE_Match object; span=(0, 2), match='ab'>


s12 = len("re")
print(s12)  #2


re_str = "3455454+97"
if "+" not in re_str and "-" not in re_str and "*" not in re_str \
        and "/" not in re_str and "(" not in re_str and ")" not in re_str:
    print("AA")
else:
    print("BB")

num = 50/2
print(num)    #25.0
num1 = 50 * 2
print(num1)

