print("------------Break-----------")
# x = int(input("How many candies you want ?"))
# i = 1;
#
# while (i <= x) :
#     print("Candy Ghe", i)
#     i += 1
# print("Total zale", x)


av = 10
x = int(input("How many candies you want ?"))
i = 1;

while (i <= x) :
    if i > av:
        print("Out of stock")
        break
    print("Candy Ghe",end=" ")
    i += 1
print("Visit Again !")


print("------------continue-----------")

for i in range(42,67):
    if(i%3==0 or i%5==0):
        continue
    print(i, end = " ")
print("Priting completed")

print()

print("-----------pass-----------")
for i in range(33, 78):
    if(i % 2 != 0):
        pass
    else:
        print(i, end =" ")
print("Pass ho gaya bhai tu..")





