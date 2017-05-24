
#学生和老师与学校是组合关系，学生和老师与SchoolMember是继承关系
class School(object):

    def __init__(self, name, addr):
        self.nmae = name
        self.addr = addr
        self.students = []
        self.staffs = []


    def enroll(self, stu_obj):
        print("为%s学员办理注册手续" % stu_obj.name)
        self.students.append(stu_obj)

    def hire(self, staff_obj):
        print("雇佣新员工%s" % staff_obj.name)
        self.staffs.append(staff_obj)


class SchoolMember(object):
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def tell(self):
        pass


class Teacher(SchoolMember):     #继承SchoolMember
    def __init__(self, name, age, sex, salary, course):
        super(Teacher, self).__init__(name, age, sex)
        self.salary = salary
        self.course = course

    def tell(self):
        print("""
        ----info of Teacher:%s----
        Name:%s
        Age:%s
        Sex:%s
        Salary:%s
        Course:%s
        """ % (self.name,self.name, self.age, self.sex, self.salary, self.course))  #重构方法

    def teach(self):
        print("%s is teaching [%s]" % (self.name, self.course))




class Student(SchoolMember):
    def __init__(self, name, age, sex, stu_id, course):
        super(Student, self).__init__(name, age, sex)
        self.stu_id = stu_id
        self.course = course


    def tell(self):
        print("""
        ----info of Teacher:%s----
        Name:%s
        Age:%s
        Sex:%s
        Stu_id:%s
        Course:%s
        """ % (self.name, self.name, self.age, self.sex, self.stu_id, self.course))  #重构方法


    def pay_tuition(self, amount):
        print("%s had paid tuition for $%s" % (self.name, amount))


school = School("老男孩IT", "惠来")

t1 = Teacher("oldboy", 23, "M", 100000, "Linux")
t2 = Teacher("Alex", 22, "M", 3000, "Python")

s1 = Student("zcl", 30, "M", 123, "Pytthon")
s2 = Student("张程亮", 40, "M", 1001, "Linux")


t1.tell()
s1.tell()

school.hire(t1)
school.enroll(s1)
school.enroll(s2)

print(school.students)
print(school.staffs)

school.staffs[0].teach()

for stu in school.students:
    stu.pay_tuition(5000)

