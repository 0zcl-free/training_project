
import redis
#建立连接
r = redis.Redis(host="127.0.0.1",port=6379)

all_keys = r.keys() #输出所有key,列表[b'age', b'name', b'occupation']
for k in all_keys:
    print(k, r.get(k))

print(r.keys())

r.set("sister","yongli",ex=5)  #存入缓存，5秒后清除

print(r.get("sister"))

r.set("father","jingxian",nx=True)  #只有father不存在时，当前set操作才执行
print(r.get("father"))

r.set("AA","BB",xx=True)  #只有AA存在时，当前set操作才执行
print(r.get("AA"))


r.mset(k1="v1", k2="v2")  #批量设置值
print(r.mget("k1", "k2"))  #批量获取值


r.set("id", "3114007487")
print(r.getrange("id", 3,6))  #获取子序列(切片,0开始)

r.setrange("id", 3, "AAA")  #修改字符串内容，从指定字符串索引开始向后替换
print(r.getrange("id", 0, -1))  #输出:b'311AAA7487'

#"3"  对应ASCII是51,二进制为0011　0011
print(r.getbit("id", 7))
r.setbit("id", 7, 0)  #将第7位改为0
print(r.getbit("id", 7))
print(r.getbit("id", 1000))  #读取位数超过，不爆错
print(r.get("id"))


