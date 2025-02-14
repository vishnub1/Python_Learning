

for i in range(5):
    for j in range(i):
        print("* ",end=" ")
        # j += 1;
    print()


# Reverse printing
print("Reverse ")
for i in range(5):
    for j in range(5-i):
        print("* ", end="")
    print()