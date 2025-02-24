# pip3 install numpy

import numpy as np

# Creating a 1D array (Matrix)
arr = np.array([123,4,4,5,5,6])
print(arr)

# Creating a 2D array (Matrix)
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array:\n", arr_2d)

# Creating a 3D array
arr_3d = np.array(
    [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
)
print("\n3D Array:\n", arr_3d)
