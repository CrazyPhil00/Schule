import random

number_list = []
number3_average = 0
number_average = 0

amount_nums = 5

for i in range(0, amount_nums):
    number_list.append(random.randrange(1, 999))

for number in number_list:
    numbers_3 = number ** 3

    number_average = number_average + number
    number3_average = number3_average + numbers_3

number3_average = number3_average / len(number_list)
number_average = number_average / len(number_list)

print(number_average **3)
print(number3_average)
