import random

from samba.dcerpc.dcerpc import response

print(random.randint(1,10))  # random integer bet 1 to 10
print(random.choice(['apple', 'banana', 'cherry']))  # Random selection
print(random.uniform(1.5, 5.5))  # Random float between 1.5 and 5.5


# --------------------
import datetime
curr_time = datetime.datetime.now();
print(curr_time)  # 2025-02-24 17:33:34.283193

#--------------------------------
#OS module interacting with the operating system
import os
print(os.getcwd())  # get current working directory
# os.mkdir("new_folder") # create a new folder


#---------------------------------------
# sys module(system-related tasks
import sys
print("Python version : ", sys.version)  #python version
print("Path :", sys.path)  # list of module search paths


# Creating and importing your own Module
def greet(name):
    return f"Hello, {name}"

def square(num):
    return num * num

# Now importing and use the module
# import the_filename_above_file
# print(the_filename_above_file("Alice"))
# print(the_filename_above_file(4))


# Using external modules(Installing vai pip)
# checking if a module is installed or not
import requests
print("Request :", requests.__version__)

# installing a module using pip
# pip install requests

#  using an installed module(requests)
# import requests
# response = requests.get("https://api.gethub.com")
# print("Status code :",response.status_code)


# The __name__ == "__main__" Special variable
# When a module is imported, all of its code runs automatically. to prevent this use:
