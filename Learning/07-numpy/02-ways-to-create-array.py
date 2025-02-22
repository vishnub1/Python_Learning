'''
 # we ca create array using different ways
 array()
 linspace()
 logspace()
 arange()
 zeros()
 ones()
'''


import numpy as np
from numpy.ma.core import filled

# 1D Array
arr = np.array([1, 2, 3, 4, 5])
print(arr)

# 2D Array
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr_2d)

# Arrays of zeros
zeros = np.zeros((3, 4))
print(zeros)

print("Ones:")
ones = np.ones((2, 5))  # 2 rows and 5 columns
print(ones)

print("Identity Matrix:")
identity_matrix = np.eye(3)  # 3x3 identity matrix
print(identity_matrix)

print("array with a constant value")
filled = np.full((2,3), 7) # 2x3 array filled with 7
print(filled)

print("Using sequence")
arr = np.arange(10)  # Creates array [0, 1, 2, ..., 9]
print(arr)

arr_step = np.arange(1, 10, 2)  # Start=1, end=10 (exclusive), step=2
print(arr_step)


print("Linespace")
arr = np.linspace(0, 1, 5)  # 5 equally spaced points between 0 and 1
print(arr)

print("Random array")
random_array = np.random.rand(3,4)
print(random_array)

# random radint()
print("Random int array")
random_int_array = np.random.randint(1, 10, (2, 3))  # 2x3 array with random integers in [1, 10)
print(random_int_array)

print("Enmpty array")
empty_array = np.empty((3, 3))  # 3x3 array (values uninitialized)
print(empty_array)