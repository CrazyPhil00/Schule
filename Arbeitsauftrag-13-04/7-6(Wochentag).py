# Ask user for input
day = int(input("Please enter the day: "))
month = int(input("Please enter the month: "))
year = int(input("Please enter the year: "))


days = (365 * year) + (year // 4) - (year // 100) + (year // 400)
days += sum([0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334][:month-1])
if month > 2 and ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
    days += 1
days += day - 15

# Calculate weekday
weekday = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"][days % 7]

# Output weekday
print(f"The date {day}.{month}.{year} was a {weekday}.")
