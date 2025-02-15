import math
# Naive approach
num =  11
for i in range(2, num):
    if num % i == 0:
        print(f"{num} is not a prime number")
        break
else:
    print(f"{num} is a prime number")


# efficient code
num2 = 13
for i in range(2, num2 // 2+1):
    if num2 % i == 0:
        print(f"{num2} is not a prim    e number")
        break
else:
    print(f"{num2} is a prime number")


# Most efficient
num3 = 17
for i in range(2, int(math.sqrt(num3)) + 1):
    if num3 % i == 0:
        print(f"{num3} is not a prime number")
        break
else:
    print(f"{num3} is a prime number")

print(int(math.sqrt(num3)))