def salary(sold_cars):
    base_salary = 1000
    sales_bonus = sold_cars * 100
    performance_bonus = 500 if sold_cars > 20 else 0
    return base_salary + sales_bonus + performance_bonus


sold_cars = int(input("How many cars were sold? "))
print("The salary is", salary(sold_cars), "€.")
