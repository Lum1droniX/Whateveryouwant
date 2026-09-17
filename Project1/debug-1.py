# Intro to Programming
# Debug Exercise 2

# This program should add three numbers together.

# To fix this program, I first got rid of the total variable at the start and set it to an equation at the bottom.
# I then added float() to each input so that their values could support decimals and be used in the total variable's equation.
# As for the new "total" equation, I made it equal the sum of each float input.
# The result of these changes is a program that adds the three input numbers together.

num1 = float(input("What's the first number? >"))
num2 = float(input("What's the second number? >"))
num3 = float(input("What's the third number? >"))
total = num1 + num2 + num3
print(f"Total is: {total}")