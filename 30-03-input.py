import decimal
import math

input_a, input_b, number_decimal = 0, 0, 0


def ask_for_input():
    global input_a, input_b, number_decimal
    try:
        input_a = float(input("Enter the first number:\n"))
        input_b = float(input("Enter the second number:\n"))
        # number_decimal = int(input("How many decimals should be shown?\n"))
    except ValueError:
        print("Please Enter a Number")
        ask_for_input()


ask_for_input()

result_one = input_a + input_b
result_two = input_a - input_b
result_three = input_a * input_b
result_four = input_a / input_b

dec_one = abs(decimal.Decimal(result_one).as_tuple().exponent)
dec_two = abs(decimal.Decimal(result_two).as_tuple().exponent)
dec_three = abs(decimal.Decimal(result_three).as_tuple().exponent)
dec_four = abs(decimal.Decimal(result_four).as_tuple().exponent)

number_decimal = min(dec_one, dec_two, dec_three, dec_four)

print(f"A + B = {result_one:.{number_decimal}f} [{input_a} + {input_b} = {result_one:.{number_decimal}f}]\n"
      f"A - B = {result_two:.{number_decimal}f} [{input_a} - {input_b} = {result_two:.{number_decimal}f}]\n"
      f"A * B = {result_three:.{number_decimal}f} [{input_a} * {input_b} = {result_three:.{number_decimal}f}]\n"
      f"A / B = {result_four:.{number_decimal}f} [{input_a} / {input_b} = {result_four:.{number_decimal}f}]")

