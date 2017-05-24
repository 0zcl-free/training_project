

        # self.__food = None   #私有属性
    #
    # @property  #属性方法
    # #把一个方法变成一个静态属性
    # def eat(self):
    #     print("%s is eating %s" % (self.name, self.__food))
    #
    # @eat.setter
    # def eat(self, food):
    #     print("set to food:", food)
    #     self.__food = food
    #
    # @eat.deleter
    # def eat(self):
    #     del self.__food
    #     print("删完了")
    #没有这个方法的话会曝错TypeError: 'Dog' object is not callable
    #callable 可调用的

class Dog(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # def __call__(self, *args, **kwargs):
    #     print("running", args, kwargs)

    def __str__(self):
        return "<obj:%s>" % self.name

d = Dog("zcl", 22)
print(d)





# print(Dog.__dict__) #打印类里的所有属性，不包括实例属性
# print(d.__dict__)  #打印所有实例属性，不包括类属性

#d = Dog("CaiJingYi")()
#d(1,3,5,name = 33)


# succuss
# running (1, 3, 5) {'name': 33}



#
# d.eat
# d.eat = "taobao"
# d.eat
#
# del d.eat
# d.eat   #AttributeError: 'Dog' object has no attribute '_Dog__food'
#
# #del d.eat  #属性方法默认不能删除 AttributeError: can't delete attribute

