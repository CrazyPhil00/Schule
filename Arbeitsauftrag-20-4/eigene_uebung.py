import random

number = random.randint(1, 11)
while True:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess == number:
        print("Congratulations! You guessed the correct number.")
        break
    elif guess < number:
        print("Your guess is too low.")
    else:
        print("Your guess is too high.")
