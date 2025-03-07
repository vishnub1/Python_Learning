class Addition:

    def __int__(self, m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def sum(self, a, b, c):
        s = a + b + c
        return s

s1 = Addition(19,23,34)
print(s1.sum(33,56,87))