# for else statement
print("------------------------")
nums = [123,4,5,6,7,8,8,50]
for num in nums :
    if num % 5 == 0:
        print(num)
else:
    print("not found")



print("------------------------")
numbers = [1, 2, 4, 5,6,7,8,10]
for num in numbers:
    print(num, end=" ")
    if num == 3:
        print("Breaking loop")
        break
else:
    print("Loop completed without break.")

