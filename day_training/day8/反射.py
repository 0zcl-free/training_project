
class Dog(object):

    def __init__(self, name):
        self.name = name

    def eat(self):
        print("%s is eating..." % self.name)

def bulk(self):
    print("%s is yelling..." % self.name)


d = Dog("zcl")
choice = input(">>>:").strip()

if hasattr(d, choice):
    getattr(d, choice)
else:
    setattr(d, choice, bulk)
    d.bulk(d)







# print(hasattr(d, choice))
# #<bound method Dog.eat of <__main__.Dog object at 0x0000000003099518>>
# print(getattr(d, choice))  #内存eat对象地址
# getattr(d, choice)()
