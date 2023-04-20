import random

number = random.randint(1, 10)
guess = int(input("Guess a number between 1 and 10: "))
while guess != random:
    if guess == number:
        print("Congratulations! You guessed the correct number.")
        break
    elif guess < number:
        print("Your guess is too low.")
    else:
        print("Your guess is too high.")
    guess = int(input("Guess a number between 1 and 10: "))
