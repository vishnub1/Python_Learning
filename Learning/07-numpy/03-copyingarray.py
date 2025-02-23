from numpy import *

arr = array([1,2,3,4,5])
arr = arr + 5  # this will add 5 in every element
print(arr)


# array adding
arr_2 = array([1,222,123,14,35])
arr_3 = array([6,7,8,9,34])
arr_4 = arr_2 + arr_3      # vectorised operation
print("Array addition :",arr_4)

print("sing values :", sign(arr_2));
print("Cos values :", cos(arr_2));
print("Tan values :", tan(arr_2));
print("log values :", log(arr_2));
print("sqrt values :", sqrt(arr_2));
print("sume values :", sum(arr_2));
print("min values :", min(arr_2));
print("max values :", max(arr_2));
print("mean values :", mean(arr_2));
print("median values :", median(arr_2));
print("sort values :", sort(arr_2));
print("concat values :", concatenate((arr_2,arr_3)));

# copying array  correct way (different address)
arr_5 = array([134,2342,553,2423])
arr_6 = arr_5.copy()
print(id(arr_5))
print(id(arr_6))

# copy with same address
arr_7 = arr_5
print("arr5 :", id(arr_5))
print("arr7 :", id(arr_7))
