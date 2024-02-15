n = int(input("Enter the maximum number for the Fibonacci sequence: "))

seq= [0, 1]


print("Fibonacci sequence up to",n, ":")
while seq[-1] + seq[-2] <= n:
    seq.append(seq[-1] + seq[-2])

for num in seq:
    print(num)
