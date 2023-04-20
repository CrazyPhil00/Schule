import math

radius = float(input("Please enter the radius of the circle: "))

if radius <= 0:
    print("Error: The radius must be positive.")
else:
    circumference = 2 * math.pi * radius
    area = math.pi * radius**2
    print("Circumference:", circumference)
    print("Area:", area)
