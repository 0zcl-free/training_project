

import redis


class RedisHelper(object):

    def __init__(self):
        self.__conn = redis.Redis(host='127.0.0.1')
        self.chan_sub = 'fm88.7'  #设置两个频道，订阅频道
        self.chan_pub = 'fm88.7'  #发布频道

    def public(self, msg):
        self.__conn.publish(self.chan_pub, msg) #发布消息
        return True

    def subscribe(self):
        pub = self.__conn.pubsub()  #生成实例　打开收音机
        pub.subscribe(self.chan_sub)  #拧到那个台
        m = pub.parse_response()         #准备听 未阻塞，再调用一次就阻塞
        print(m)
        return pub   #返回实例

