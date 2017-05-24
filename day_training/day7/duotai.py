
class Animal:
    def __init__(self, name):  # Constructor of the class
        self.name = name

    def talk(self):  # Abstract method, defined by convention only
        raise NotImplementedError("Subclass must implement abstract method")

    @staticmethod
    def animal_talk(obj):
        obj.talk()

class Cat(Animal):
    def talk(self):
        print('Meow!')

class Dog(Animal):
    def talk(self):
        print('Woof! Woof!')

d = Dog("alex")
d.talk()
c = Cat("mimi")
c.talk()

#有没有可能直接 animal.talk()
Animal.animal_talk(d)       #一种接口，多种实现
Animal.animal_talk(c)
