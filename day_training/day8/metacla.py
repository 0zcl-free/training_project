
class MyType(type):

    def __init__(self, what, bases=None, dict=None):
        print("--MyType init---")
        super(MyType, self).__init__(what, bases, dict)

    def __call__(self, *args, **kwargs):
        print("--MyType call---")
        obj = self.__new__(self, *args, **kwargs)

        self.__init__(obj, *args, **kwargs)


class Foo(object):

    __metaclass__ = MyType

    def __init__(self, name):
        self.name = name
        print("Foo ---init__")

    def __new__(cls, *args, **kwargs):  #重构__new__方法
        print("Foo --new--")
        #print(object.__new__(cls))  #<__main__.Foo object at 0x0000000003296320> Foo的内存对象
        return object.__new__(cls) #通过__new__实例化，不加这句，构造函数没执行
                                    #cls 相当于Foo, 继承父类的__new__方法

# 第一阶段：解释器从上到下执行代码创建Foo类
# 第二阶段：通过Foo类创建obj对象
obj = Foo("Alex")
print(obj.name)


#__new__ 是类自带的方法
#__new__实例化会自动执行，先于__init__
