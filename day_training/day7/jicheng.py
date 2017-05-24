
#class People:             #经典类
class People(object):    #新式类

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.friends = []

    def eat(self):
        print(" %s is eating..." % self.name)

    def sleep(self):
        print("%s is sleeping..." % self.name)

    def talk(self):
        print(" %s is talking..." % self.name)


class Relation(object):
    def make_friends(self, obj):   #self = m1  obj = w1
        print("%s is making friends with %s" % (self.name, obj.name))
        self.friends.append(obj)




class Man( Relation, People):     #继承

    # def __init__(self, name, age, money):   #父类的参数 + 新加的属性
    #     #People.__init__(self, name, age)      #执行父类构造函数
    #     super(Man, self).__init__(name, age)    #新式类写法
    #     self.money = money

    def fuck(self):    #可以自己定义新的方法
        print("%s is piaoing...20s....done.." % self.name)

    def sleep(self):   #把父类覆盖,但如何先执行父类，再执行子类？？
        People.sleep(self)  #相当于重构父类方法
        print("man is sleeping..")


class Woman(People, Relation):       #多继承

    def get_birth(self):
        print("%s is getting a birth..." % self.name)

m1 = Man("zcl", 22)   #需要传参数
w1 = Woman("buty", 22)

m1.make_friends(w1)      #zcl is making friends with buty
#为什么Relation没有构造函数，也没传参数，就可以调用self.name
#比如：小孩，从他爸继承了名字，就不用再继承他妈的这妈的名字
#为什么要多继承

print(m1.friends)

