print("\nSquare")
for i in range(1, 6):
    print()
    for j in range(1, 6):
        print("D", end=" ")

print("\n\nLeft Triangle")
for i in range(1, 6):
    print()
    for j in range(1, i+1):
        print("D", end=" ")

print("\n\nRight Triangle")
for i in range(1, 6, 1):
    print()
    for j in range(1, 6-i):
        print(" ", end=" ")
    for j in range(1, i+1):
        print("D", end=" ")

print("\n\nUpside-down Triangle")
for i in range(5, 0, -1):
    print()
    for j in range(1, i+1):
        print("D", end=" ")