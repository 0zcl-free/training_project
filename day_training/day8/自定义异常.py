#
# class ZlcException(Exception):  #自定义异常
#
#     def __init__(self, msg):
#         self.message = msg
#
#     # def __str__(self):    #不用写，基类已经写了
#     #     return "dddddd"
# try:
#     raise ZlcException("数据库连不上")  #自动触发异常
#
# except ZlcException as e:
#     print(e)


class IndexError(Exception):  #自定义异常

    def __init__(self, msg):
        self.message = msg


try:
    name = []
    print(name[3])
except IndexError as e:
    print(e)
