# Basic for loop
for i in range(5):
    print(f"Iteration {i + 1}: Hello, World!")

# Looping over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I like {fruit}.")

# Looping over string
word = "Python"
for letter in word:
    print(f"Current letter: {letter}")

# Using range(start, stop, step)
for i in range(2,5):
    print(f"Current number: {i}")

for i in range(1, 10, 2):
    print(f"Odd number: {i}")

for i in range(0,10,2):
    print(f"Even number: {i}")

for i in range(10, 0, -1):
    print(f"Countdown: {i}")

# Loop with index
colors = ["red", "green", "blue"]
for i, col in enumerate(colors):
    print(f"Color {i + 1}: {col}")

# Nested for loop
for i in range(3):
    for j in range(2):
        print(f"Outer loop {i + 1}, Inner loop {j + 1}")

# For else clause
for i in range(3):
    print(f"Iteration {i}")
else:
    print("Loop completed without break.")