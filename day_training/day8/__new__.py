
def func(self):
    print("hello %s" % self.name)


def __init__(self, name, age):
    self.name = name
    self.age = age

Foo = type('Foo', (object,), {'fuck': func,
                              '__init__':__init__})
#(object,)须加逗号，里面是元组的形式，不加的话认为是一个值
f = Foo("zcl", 22)
f.fuck()
print(type(Foo))


#1.实例化类Foo,(object)继承object 3.里面的方法

# class Foo(object):
#     def __init__(self, name):
#         self.name = name
#
# f = Foo("alex")
# print(type(f))   #<class '__main__.Foo'>来自Foo
# print(type(Foo))  #<class 'type'> 来自type