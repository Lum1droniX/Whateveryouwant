# Intro to Programming
# Debug Exercise 2

# Let's figure out if a number is greater than 5 and less than 10.
# This has two parts; read the comments and don't be afraid to
# contact me on Canvas or email if you have questions.


user_val = int(input("Enter a whole number. >"))

# Part 1: Discover why this condition doesn't work and fix it.
# Part 2: (Don't do this until part 1 is done)
#         We're testing the same variable twice, to make sure it falls
#         between a range of values. Rewrite the condition to make this simpler.
if user_val > "5" and user_val < "10":
    print(f"{user_val} is less than 10, but greater than 5.")
else:
    print(f"{user_val} falls outside the bounds we're looking for.")
