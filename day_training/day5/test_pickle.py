


# r = pickle.dumps(li)
# print(r, type(r))    #字节类型
#
# result = pickle.loads(r)
# print(result)


# li = [11,22,33,44,55]
# #以字节方式写到文件
# pickle.dump(li, open('db', 'wb'))
#
# r = pickle.load(open('db', 'rb'))
# print(r, type(r))
#import pickle


import json
class Foo():
    def __init__(self):
        pass

f = Foo()     #一个对象
json.dumps(f)

