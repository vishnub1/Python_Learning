import py_06_teluso_module as cal

a = 5
b = 10

# c = cal.add(f"Addition of {a} and {b} :",a, b)
c = cal.add(f"Addition of {a} and {b} :", a, b)
print(c)

print("Subtractions : ")
d = cal.sub(a, b)
print(d)

print("Multiplication : ")
e = cal.multi(a,b)
print(e)

print("Division : ")
f = cal.div(a, b)
print(f)
