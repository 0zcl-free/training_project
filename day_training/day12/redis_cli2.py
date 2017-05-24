
import redis
#建立连接
pool = redis.ConnectionPool(host='127.0.0.1', port=6379)
r = redis.Redis(connection_pool=pool)


r.setbit("uv_count1", 5,1)
r.setbit("uv_count1", 8,1)
r.setbit("uv_count1", 3,1)
r.setbit("uv_count1", 3,1)
print("uv_count:", r.bitcount("uv_count1"))
