class Student:

    school = "ZPPS Belsakarga"

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3

    def info(cls):
        return cls.school

s1 = Student(31,47,32)
s2 = Student(21,32,47)

print(s1.avg())
print(s2.avg())
print(s1.info())