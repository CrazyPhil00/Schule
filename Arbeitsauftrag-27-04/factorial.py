
n = int(input("Enter a number: "))

fakultaet = 1
for i in range(1, n+1):
    fakultaet *= i

print(f"The factorial from {n} ist {fakultaet}")

