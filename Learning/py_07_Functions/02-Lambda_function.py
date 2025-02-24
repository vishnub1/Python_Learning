# A lambda function is a small, anonymous function with a single expression.

add = lambda x, y : x + y
print(add(5, 3))

def outer() :
    print("Outer Function")

    def inner() :
        print("Inner function")

    inner()
outer()


# ---------------------------------------

x = 10
def my_function():
    y = 5  # local variable
    print(x + y)  #[ans = 15] can access global variable

my_function()
print(x)  # works [ans = 10]
# print(y)   # Error (y is local to my_function)



# ------------------------------------------

def celsius_to_fah(celsius):
    return (celsius * 9/5) + 32

print(celsius_to_fah(25)) # output : 77.0

