def factorial(n) :
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))

# Summary Table
# Function Type	            : Syntax Example
# No Parameters	def greet() : print("Hi")
# With Parameters	        : def greet(name): print(name)
# With Return Value	        : def add(a, b): return a + b
# Default Parameter	        : def greet(name="Guest"):
# *args (Multiple)	        : def add_all(*args):
# **kwargs (Key-Value)	    : def details(**kwargs):
# Lambda Function	        : lambda x, y: x + y
# Nested Function	        : def outer(): def inner():
# Recursion	def factorial(n): return n * factorial(n-1)