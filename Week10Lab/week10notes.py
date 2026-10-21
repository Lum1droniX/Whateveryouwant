# Call a function: running a function by using its name with parenthesis
# Parameters: values that are passed into a function when it is called
# Arguments: the actual values that are passed through a function when it is called

def say_hello():
    print("Hello")

# Call the function
say_hello()

# Arguments and Parameters
# Function that is going to greet me by name
# Function is going to be called Greet
def greet(name):
    # Name is the parameter (which is a placeholder)
    # Print out "Hello [name]"
    print(f"Hello {name}")

# Call my function and its going to say "Hello Hayden"
# An argument is a real value, Hayden is the argument in the function below
# Parameters are like blanks, arguments fill them in 
greet("Hayden")

# Why are functions useful?
    # Reusing code (don't have to copy and paste blocks of code)
    # Organization, allows our program to become more readable
    # Breaking big problems into smaller parts

print("Welcome")
print("Pick an option")
print("Goodbye")

# VS

def show_menu():
    print("Welcome")
    print("Pick an option")
    print("Goodbye")
show_menu()

# Print vs Return
# A function that prints
def hello_world():
    print("Hello")
    # This shows the text to the user, but doesn't give a value back to the rest of the code

# A function that returns
def hello_return():
    return "Hello"
    # This sends a value back to wherever the function is called
    # The caller can store it, use it, print it, etc.

# Print is for the user, return is for the program
msg = hello_return()
print(msg)

result = hello_world()
print(hello_world)
# This returns the position of the function in running memory because there aren't any values assigned to it

# Calc function that uses 2 parameters, and will have if/elif based on the operator
def calculator(Number1, Number2):
    operator = input("Choose an operation (+, -, *, /): ")
    # Use if/elif to decide what to do
    # Perform the math
    # Print or return the result

# Fake loop, function calling itself
# A function can call itself, which is calle drecursion
# Behaves like a loop if it reprats until a condition is met

def play_again():
    # User to be prompted with question if they say y then reprompt, if n break out of loop
    question = input("Do you want to play again: Y or N").lower()
    if question == "y":
        play_again()
    else:
        print("Goodbye")

