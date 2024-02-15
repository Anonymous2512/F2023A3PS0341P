n = int(input("Enter the number of rows: "))

for x in range(1,n+1):
    for i in range(n - x):
        print(" ", end=" ")
    for j in range(0,x):
        print(j+1, end=" ")
    print()
