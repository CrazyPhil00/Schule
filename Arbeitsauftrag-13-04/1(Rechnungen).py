"""

Rechner für flächen und Umfängen von Körpern (Aufgabe 1)

"""

import math


# colors for print
class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


type_of_calculation = 0
try:
    # question the user which type he wants to calculate
    type_of_calculation = int(input(f"{colors.BOLD}What do you want to calculate?\n"
                                    f"{colors.ENDC}[{colors.UNDERLINE}0{colors.ENDC}] square\n"
                                    f"[{colors.UNDERLINE}1{colors.ENDC}] rectangle\n"
                                    f"[{colors.UNDERLINE}2{colors.ENDC}] circle\n"
                                    f"[{colors.UNDERLINE}3{colors.ENDC}] triangle\n"))
except ValueError:
    print(f"{colors.UNDERLINE}Please enter a number")
    exit(-1)

if type_of_calculation == 0:
    # User selected square
    side_a = int(input(f"{colors.HEADER}What is side A?\n"))

    area = side_a * side_a
    scope = side_a * 4

    print(f"The area is {area}\n"
          f"The scope is {scope}\n")


elif type_of_calculation == 1:
    # user selected rectangle
    side_a = int(input("What is side A\n"))
    side_b = int(input("What is side B\n"))

    area = side_a * side_b
    scope = (side_a * 2) + (side_b * 2)

    print(f"The area is {area}\n"
          f"The scope is {scope}\n")

elif type_of_calculation == 2:
    # user selected circle
    radius = int(input("What is the radius?\n"))

    area = radius ** 2 * math.pi
    scope = radius * 2 * math.pi

    print(f"The area is {area}\n"
          f"The scope is {scope}\n")

elif type_of_calculation == 3:
    # user selected triangle
    side_a = int(input("What is side A?\n"))
    height = int(input("What is the height?\n"))

    area = (side_a * height) / 2
    scope = side_a * 3

    print(f"The area is {area}\n"
          f"The scope is {scope}\n")
