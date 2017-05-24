
import datetime
#
# print(datetime.date.today())  #输出格式2016-10-13
#
#
#current_time = datetime.datetime.now()
# print(current_time)   #2016-10-13 10:49:32.200262


# #时间的加减
# print(datetime.datetime.now())
# print(datetime.datetime.now() + datetime.timedelta(days=10))
# print(datetime.datetime.now() - datetime.timedelta(days=10))
# print(datetime.datetime.now() + datetime.timedelta(hours=10))

# current_time = datetime.datetime.now()
# #2015-05-13 11:16:34.646562  去年5月
# print(current_time.replace(2015, 5))
"""
# atetime模块是对time模块进行封装，
# time模块常用取时间戳  datetime取日期
"""


#时间的比较
current_time = datetime.datetime.now()
time_obj = current_time.replace(2017,5)
print(time_obj)
print(current_time > time_obj)
