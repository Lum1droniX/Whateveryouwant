# CISW 125
# Intro to programming

# Follow the Documentation Policy as it's good practice and will get you used to what you should do for
# your projects and other labs.

# If you're stuck, ask questions. There are no dumb questions.
# ------------------------------------------------------------------------------------------------------
# We're going to play around with variables and expressions today
# The goal is to just test out things and put them to use and possibly
# save the ideas/work for projects down the line.

# Again, the goal is to "play" around and explore. There's no right or wrong to this.
# Just think about input vs output and what we can do with them.
# ------------------------------------------------------------------------------------------------------


# Create some variables, give them a theme. Example: items on a grocery list, games/books/movies you enjoy, etc.

favoriteGame="Grounded 2"
favoriteFood="Little Caesars"
favoriteMovie="The Lego Movie"

# Then print your variables.

print(favoriteGame)
print(favoriteFood)
print(favoriteMovie)

# Now try to reassign a value. This is essentially "overwriting" your variables data with new data. Python works from top to bottom.

favoriteGame="osu!mania"
favoriteFood="Sushi"
favoriteMovie="Quest for the Holy Grail"

# After you've done this, try to print your variables in string using f-strings.

print(f"My favorite game is {favoriteGame}.")
print(f"My favorite food is {favoriteFood}.")
print(f"My favorite movie is {favoriteMovie}.")

# Next, try to create some expressions that involve addition, subtraction, multiplication, and division
# Store the results of your expressions in a variable and then print the outcome

Value1=21
Value2=42
Value3=13

Add=Value1+Value2+Value3
Subtract=Value3-Value2-Value1
Multiply=Value2*Value3
Divide=Value2/Value1

print(f"Adding {Value1}, {Value2}, and {Value3} results in {Add}")
print(f"Subtracting {Value3}, {Value2}, and {Value1} results in {Subtract}")
print(f"Multiplying {Value2} by {Value3} results in {Multiply}")
print(f"Dividing {Value2} by {Value1} results in {Divide}")

# See if you can find other ways to "do maths" (hint: operators are useful and efficient.)
# https://www.w3schools.com/python/python_operators.asp

Square=Value1**2

print(f"The square of {Value1} is {Square}")

# Now, I'd like you to make two variables that contain your first and last name
# After you've made the variables, find a way to join the two strings to print your full name. This is string concatenation.
# Think of it as "adding" your variables together.

nameFirst="Hayden "
nameLast="Fillmore"

nameFull=nameFirst+nameLast
print(nameFull)

# While we did some math earlier, I'd like you to try doing math with variables this time. (If you already did this, you can skip this. Good job.)

    # Already did it :)

# Lastly, do something of your own choice. Anything that involves variables and expressions is allowed here.
# If you're stumped on ideas, just try and make an expression that converts Celsius to Fahrenheit or vice versa.

print("")
print("================================")
print("")

Value1=input("What is your first value? ")
Value2=input("What is your second value? ")
Add=int(Value1)+int(Value2)
Subtract=int(Value1)-int(Value2)
Multiply=int(Value1)*int(Value2)
Divide=int(Value1)/int(Value2)

Result=input("What operation would you like to perform? (Add, Subtract, Multiply, Divide): ")
if Result=="Add":
    print("")
    print(f"The result of adding {Value1} and {Value2} is {Add}")
    print("")
    print("================================")
if Result=="Subtract":
    print("")
    print(f"The result of subtracting {Value2} from {Value1} is {Subtract}")
    print("")
    print("================================")
if Result=="Multiply":
    print("")
    print(f"The result of multiplying {Value1} and {Value2} is {Multiply}")
    print("")
    print("================================")
if Result=="Divide":
    print("")
    print(f"The result of dividing {Value1} by {Value2} is {Divide}")
    print("")
    print("================================")

# Upload this to Canvas under the Variable and Expressions Lab assignment.
