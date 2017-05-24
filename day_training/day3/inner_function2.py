s = '程亮'
#字符串转换成字节类型
#bytes(转换的字符串，按照什么编码方式)
n1 = bytes(s, encoding='utf-8')
n2 = bytes(s, encoding='gbk')
print(n1)
print(n2)

#字节转换成字符串
#str(字节，转换成字符串的编码方式)
new_str = str(bytes(s, encoding='utf-8'), encoding='utf-8')
print(new_str)