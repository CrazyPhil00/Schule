import random


field = bytearray(5000)

# Fill the array with random values between 1 and 6
for i in range(len(field)):
    field[i] = random.randint(1, 6)

# Calculate the frequency of each possible value
frequencies = [0, 0, 0, 0, 0, 0]
for value in field:
    frequencies[value-1] += 1

# Print the results
print("After 5000 random numbers the chances are:")
for i in range(6):
    absolute_frequency = frequencies[i]
    relative_frequency = absolute_frequency / len(field) * 100
    print(f"{i+1}s: {absolute_frequency} equals {relative_frequency:.2f} %")
