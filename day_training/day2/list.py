name = ["zcl", "金意", "烁升", "森炜", "嘉详", "诚有", "浩延"]
print(name)

name.insert(3,"asd")
name.insert(4,"qwe")
print(name)

print(name[2:8])

name.remove(name[6])
print(name)

#name.remove("asd")
#name.remove("qwe")
del name[3:5]
print(name)

#del name         #全部删除

name[0] = "zcl(captical)"
print(name)

#print(name[-1])   #打印最后一个

print(name[0::2])   #每隔一个打印


