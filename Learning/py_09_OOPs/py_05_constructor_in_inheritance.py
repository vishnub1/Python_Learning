class A:

    def __init__(self):
        print("A init constructor")

    def feature(self):
        print("A feature")

    def feature2(self):
        print("A feature2")


class B:

    def __init__(self):
        # with the help of super we can call the super class
        super().__init__()
        print("B init constructor")

    def feature(self):
        print("B feature")

    def feature3(self):
        print("B feature3")

class C(A, B):
    def __init__(self):
        super().__init__()
        print("C init constructor")


# a1 = A()
# b1 = B()  # it call the constructor of a [parent child relation ] if B init not present
# c1 = C()
a1 = C()
a1.feature()

