class Role(object):
    n = 123    #类变量
    name = "i am lei"
    n_list = []
    def __init__(self, name, role, weapon, life_value=100, money=15000):
        self.name = name      #self.name是实例变量(静态属性)，作用域就是实例本身
        self.role = role
        self.__value = 100
        self.weapon = weapon
        self.life_value = life_value
        self.money = money

    def __del__(self):
        print("finish.....")

    def __shot(self):                        #类的方法，功能（动态属性）
        print("shooting...")

    def show_status(self):
        print("nanme:%s life_value:%s" % (self.name, self.__value))

    def got_shot(self):
        print("ah...,I got shot...")
        self.__shot()

    def buy_gun(self):
        print("just bought %s" % self.name)


print(Role)

r1 = Role('Alex', 'police', 'AK47') #生成一个角色
#print(r1.__value)   #对外界隐藏，AttributeError: 'Role' object has no attribute '__value'
r1.show_status()

#del r1
r1.buy_gun()
r1.got_shot()
r2 = Role('lex', 'police', 'AK47') #生成一个角色

r2.buy_gun()
r2.got_shot() #程序退出时，执行执构函数，若程序N年不退出，实例也不会被销毁？？？
             #只要变量名在，python虚拟机就有不会被销毁，反之，会被销毁

r1.got_shot()
# r1.name = 'zcl'   #可以改变实例的变量，相当于self.name = 'zcl'
#
# r1.bullet = 'fight'  #可以增加实例新属性，注意实例化过程 == self.bullet = 'fight'
# print(r1.bullet)
#
# print(r1.weapon)
# del r1.weapon
# #print(r1.weapon)     #可以删除实例属性
# r2 = Role('Jack', 'terrorist', 'B22')  #生成一个角色
# #问：实例可以改变类变量？？
# r1.n = "改变变量"     #相当于在r1内存创建实例变量n
# print("r1:", r1.n)   #r1: 改变变量
# print("r2:", r2.n)   #r2: 123
#
# Role.n = "ABC"
#
# print(r1.n, r1.name)  #不实例化也能调用n,不实例也能调用n
# print(r2.n, r2.name)  #类本身有name,实例本身也有name，先去实例找，再去类本身找
# print(Role.n)   #类变量
# #r1.buy_gun()
# Role.buy_gun(r1)
# #r2.buy_gun()
#
# r1.n_list.append("from r1")
# r2.n_list.append("from r2")
# print(r1.n_list,r2.n_list)
# print(Role.n_list)     #三个共用一个内存变量
#

