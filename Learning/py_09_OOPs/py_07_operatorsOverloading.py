# a = 5
# b = ('world')
# c = 20
#
# # print(a + b)  error
#
# print(a + c)
# print(int.__add__(a,c))

class Student:

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1, m2)

        return s3

s1 = Student(12,23)
s2 = Student(30,20)

s3 = s1 + s2

print(s3.m1)

