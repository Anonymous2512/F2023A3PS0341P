rows = int(input("Enter the number of rows (even): "))

for i in range(1, rows//2 + 1):
    print(" " * (rows//2 - i), end="")
    print("*" * (2*i - 1))

for i in range(rows//2, 0, -1):
    print(" " * (rows//2 - i ), end="")
    print("*" * (2*i - 1))
