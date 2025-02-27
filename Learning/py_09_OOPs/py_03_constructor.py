# class Com:
#     pass
#
# c1 = Com()
# c2 = Com()
# print(id(c2))
# print(id(c1))

# Every time you create an object it is allocated to new space


# Compare

class Computer:

    def __int__(self):
        self.name = "Navin"
        self.age = 20

    def update(self):
        self.age = 30

    def compare(self,other):
        if self.age == other.age:
            return True
        else :
            return False

c1 = Computer()
c2 = Computer()

if c1.compare(c2):
    print("They are smme")
