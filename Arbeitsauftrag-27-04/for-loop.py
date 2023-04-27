amount = int(input("Wie viele Zahlen willst du addieren?"))

result = 0

for i in range(1, amount + 1):
    result += i
    print(f"{result} + ", end='')

print(f"= {result}")
