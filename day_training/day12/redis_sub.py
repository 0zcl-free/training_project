
from redis_helper import RedisHelper

obj = RedisHelper()
redis_sub = obj.subscribe()  #返回实例

while True:
    print("AA")
    msg = redis_sub.parse_response()   #听
    print(msg)  #有消息则打印，无消息则阻塞