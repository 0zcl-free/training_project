
import hashlib

obj = hashlib.md5(bytes("zcl", encoding='utf-8'))  #创建md5对象
print(obj)
obj.update(bytes("123", encoding='utf-8'))#进行加密（先变成字节）
rusult = obj.hexdigest() #获取加密后的值
print(rusult)

#md5  可加行加密，但不能反解
#虽然用户不能反解，但用可能撞库，
# 利用明文与密文一一对应，黑客可能通过密文比较推出明文
#obj = hashlib.md5(bytes("zcl", encoding='utf-8'))
#可在上面加入key,再在key的基础上进行加密

