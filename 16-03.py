import math

try:
    type_of_calculation = int(input("What do you want to calculate?\n"
                                    "[0] square\n"
                                    "[1] rectangle\n"
                                    "[2] circle\n"
                                    "[3] triangle\n"))
except ValueError:
    print("Please enter a number")
    exit(-1)


if type_of_calculation == 0:
    side_a = int(input("What is side A?\n"))

    area = side_a * side_a
    scope = side_a * 4

    print(f"The area is {area}\n")
    print(f"The scope is {scope}\n")

elif type_of_calculation == 1:
    side_a = int(input("What is side A\n"))
    side_b = int(input("What is side B\n"))

    area = side_a * side_b
    scope = (side_a * 2) + (side_b * 2)

    print(f"The area is {area}\n")
    print(f"The scope is {scope}\n")

elif type_of_calculation == 2:
    radius = int(input("What is the radius?\n"))

    area = radius ** 2 * math.pi
    scope = radius * 2 * math.pi

    print(f"The area is {area}\n")
    print(f"The scope is {scope}\n")

elif type_of_calculation == 3:
    side_a = int(input("What is side A?\n"))
    height = int(input("What is the height?\n"))

    area = (side_a * height) / 2
    scope = side_a * 3

    print(f"The area is {area}\n")
    print(f"The scope is {scope}\n")
