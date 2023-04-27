amount = int(input("How many numbers do you want to add?"))

result = 0

for i in range(1, amount + 1):
    result += i
    if amount == i:
        print(f"{i} ", end='')
    else:
        print(f"{i} + ", end='')

print(f"\n= {result}")
