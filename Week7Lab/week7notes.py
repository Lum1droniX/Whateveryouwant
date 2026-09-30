# What is a loop?
    # A loop is a section of code that repeats.

# Repeat this loop 3 times

# for number in range(3):
    # Print Hello each time the loop runs
    # print("Hello!")

# While loops
    # A while loop repeats while a condition is true.

# Make a program that is going to print 1-5

# Create a variable starting at 1
# number = 1
# while number <= 5:    # This is essenaitally where it will stop
#     print(number)
#     number += 1

# I want to start counting at 0, count to 50, and get there by increments of 5

# number2 = 0
# while number2 <= 50:
#     print(number2)
#     number2 += 5

# A while loop is useful when you want to keep asking untl the user gives a valid answer
# Ask the user for their age

# age = int(input("What is your age?> "))

# Keep looping if the age is less than 1 or greater than 120
# while 1 > age > 120:
    # Tell the user "Invalid input!"
    # print("Invalid input!")

    # Ask the user to enter their age again
    # age = int(input("What is your age?> "))
# This runs after the loop finishes
# print("Thank you :D")

# For loop
    # A for loop works through items one at a time

# Create a list containing 3 games
# games = ["Minecraft", "Mario", "Zelda"]
# Take one item from the games list at a time
# for game in games:
    # Print the current game
    # print(game)
# Each time the loop repeats, game holds the next item in the list

# Range
    # range() creates a sequence of numbers

# Starts at 2 and stops right before 8
# for number in range(2, 8):
    # Print the current number
    # print(number)

# We can also perform calculations inside the loop
# Loop through numbers 2 through 7
# for number2 in range(2, 8):
    # Multiply the number by itself
    # print(f"{number2 * number2}")

# Looping through a string
# Store a name inside the string
# name = "Hayden"
# Take one character from the string at a time
# for letter in name:
#     print(letter)

# Using break
    # Break stops a loop early

# Loop through numbers 1-10
# for number in range(1, 11):
    # Print the current number
    # print(number)
    # Break the loop when number hits 5
    # if number == 5:
    #     break

# Nested loops
    # A nested loop is a loop inside another loop

# Outer loop runs through 1, 2, and 3
# for number in range(1, 4):
    # Inner loop also runs through 1, 2, and 3
    # for number2 in range(1, 4):
    #     print(number, number2)

# Choosing the right loop
    # Use a while loop when repetition depends on a condition
    # Use a for loop when working through items
    # Use for with range() when working through numbers
    # 