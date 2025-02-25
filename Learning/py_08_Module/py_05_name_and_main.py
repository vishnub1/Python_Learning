# The __name__ == "__main__" Special variable
# When a module is imported, all of its code runs automatically. to prevent this use:
def greet():
    print("Hello from my_module !")

if __name__ == "__main__":
    greet()



#---------------------------
# Reloading a Module(importlib)
# if you modify a module after importing it, python wont reload it
# automatically. to reload.

# import importlib
# import user_module
#
# importlib.reload(user_module)


# ----------Summary Table---------------
'''
    Feature	                Example Usage
    Importing a module	        :  import math
    Importing specific function	:  from math import sqrt
    Importing with an alias	    :  import math as m
    Importing everything	    :  from math import *
    Checking Python version     :  import sys; print(sys.version)
    Installing an external module :	pip install requests
    Creating a custom module	: def my_function(): return "Hello"
    Checking module search paths:	import sys; print(sys.path)
    Reloading a module	        :  importlib.reload(module_name)
'''

# ====================Telusko Learning==========================
print(__name__)
