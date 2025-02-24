# def function_name(parameters):
#     """Optional docstring"""
#     # Function body
#     return value  # (Optional)
#
#
# function_name(arguments)


# def greet():
#     print("Hello, Welcome to Python!")
#
# greet()  # Calling the function


def greet(name):  # 'name' is a parameter
    print(f"Hello, {name}!")

greet("Alice")  # Passing an argument

#
#
def add(a, b):
    return a + b

result = add(5, 3)
print(result)  # Output: 8



def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()       # Output: Hello, Guest!
greet("John") # Output: Hello, John!



def add_all(*numbers):
    return sum(numbers)

print(add_all(1, 2, 3, 4, 5))  # Output: 15



def person_details(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

person_details(name="Alice", age=25, city="New York")

