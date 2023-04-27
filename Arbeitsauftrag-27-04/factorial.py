
n = int(input("Enter a number: "))

fakultaet = 1
for i in range(1, n+1):
    fakultaet *= i
    if n == i:
        print(f"{fakultaet} * {i} ", end='')
    else:
        print(f"{fakultaet} * {i} * ", end='')

print(f"\n= {fakultaet}")

