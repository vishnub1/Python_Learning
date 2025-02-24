# importing the Entire module

import math
print(math.sqrt(25))


# Importing the specific functions
from math import sqrt, pow
print("Sqrt of 6:",sqrt(36))
print("2 to the Power of 3:", pow(2,3))

# importing a module with an alias
import math as m
print("Factorial of 5: ", m.factorial(5))

# importing Everything from a Module (*)
from math import *
print("Sin :", sin(0))
print("PI value :", pi)

