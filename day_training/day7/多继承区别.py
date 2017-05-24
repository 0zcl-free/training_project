
class A:
    def __init__(self):
        print("AA")

class B(A):
    # def __init__(self):
    #     print("BB")
    pass

class C(A):
    # def __init__(self):
    #     print("CC")
    pass

class D(B, C):
    pass
    # def __init__(self):
    #     print("DD")

d = D()

