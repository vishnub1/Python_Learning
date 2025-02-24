# from array import *
#
# vals = array('i',[1,2,3,4,5])
#
# newArr = array(vals.typecode,(a for a in vals))
#
# for e in newArr:
#     print(e)

from array import *
arr = array('i', [])
n = int(input("Enter the length of the array"))
for i in range(n):
    x = int(input("Enter the element"))
    arr.append(x)

print(arr)

# printing particular index value
val = int(input("Enter the value fro search"))
k = 0
for e in arr:
    if e == val:
        print("The value is present at index", k)
        break

    k += 1