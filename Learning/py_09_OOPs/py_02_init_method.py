from asyncio.unix_events import can_use_pidfd


class Computer:
    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def config(slef):
        print("Config is ", slef.cpu, slef.ram)


comp1 = Computer('i5', 16)
comp2 = Computer('Rayzen 3', 8)

comp1.config()
comp2.config()