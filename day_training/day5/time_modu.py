
import time

#print(time.time())    #返回当前时间戳1476322968.500532


# print(time.ctime())   #返回当前时间Thu Oct 13 09:42:48 2016
# print(time.ctime(time.time() - 86400))

'''
time_obj = time.gmtime()
print(time_obj)    #将utc时间戳转换成struct_time格式
print(time_obj.tm_year, time_obj.tm_mon) #根据struct_time格式取出
print("{year}-{month}".format(year = time_obj.tm_year, month = time_obj.tm_mon))

'''
#
# print(time.localtime())    #当地的时间，中国以东八区为准
# print("---------")


#
# tm = time.gmtime()
# print(time.mktime(tm))      #传时间对象参数,将对象转成时间戳


"""
print("*************")
time.sleep(4)
print("*************")
"""

"""
tm = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
#将utc(世界标准时间) struct_time格式转成指定的字符串格式
tm1 = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())  #utf时间
print(tm)
print(tm1)
"""
# 将 日期字符串 转成 struct时间对象格式
# tm2 = time.strptime("2016-05-6 15:06", "%Y-%m-%d %H:%M")
# print(tm2)


#将时间字符串形式转成时间戳
tm = time.strptime("2016-05-6 15:06", "%Y-%m-%d %H:%M")
print(time.mktime(tm))


