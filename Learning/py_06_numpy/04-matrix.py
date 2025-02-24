from numpy import *

arr1 = array([[1,2,3],[4,5,6]])
print(arr1)
print("Shape :",arr1.shape)
print("Data Type :", arr1.dtype)
print("dimentional : ", ndim(arr1))

# converting 2D array to 1D array
arr2 = arr1.flatten()
print("Flattened array :", arr2)

# Arrays reshaping
arr3 = arr1.reshape(3,2)
print("Original array :")
print(arr1)
print("Shape :",arr1.shape)
print("Dimension", arr1.ndim)

print("Reshaped array :")
print(arr3)
print("Shape :",arr3.shape)
print("Dimension", arr3.ndim)

print()
# converting to 3D array
arr4 = arr3.reshape(1,3,2)
print("3D array :")
print(arr4)
print("Shape :",arr4.shape)
print("Dimension", arr4.ndim)