class Computer:
    def config(self):
        print("i5, 16GB, 1TB")

com1 = Computer()
com2 = Computer()

Computer.config(com1)
Computer.config(com2)

# another way  [most time we use this ]
com1.config()
com2.config()

