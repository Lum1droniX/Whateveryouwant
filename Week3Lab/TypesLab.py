# ----------------------------------------------------------

Variable_Int=21
Variable_Float=3.14

    # You can do math with a float and interger at the same time.

Equation1 = Variable_Int + Variable_Float
print(Equation1)

Variable_Int = input("What is your interger value?: ")
Variable_Float = input("What is your float value?: ")

Int_Input = int(Variable_Int)
Float_Input = float(Variable_Float)

Equation2 = Int_Input + Float_Input

print(Equation2)

# ----------------------------------------------------------

    # A string is text data.

Message = "Hello World"
CallMessage = (f'Your message was "{Message}"')  # This is the string variable that calls the other string I created.

print(CallMessage)

FirstChar = Message[0]
print(FirstChar)

SeventhChar = Message[6]
print(SeventhChar)

FirstWord = Message[0:5]
print(FirstWord)

LastWord = Message[6:11]
print(LastWord)

# ----------------------------------------------------------

    # Lists can contain text and numerical data such as strings, intergers, floats, and even mixed data types.

ShoppingList = ["Milk", "Bananas", "Eggs", "Watermelon"]
NumberList = [25, 42, 13, 69]

ShoppingList.append("Paper towels")
print(ShoppingList)

    # Using the .append() method added the string to the list.

ShoppingList.remove("Bananas")
print(ShoppingList)

print(f"My shopping list has {len(ShoppingList)} items on it.")

print(f"My number list is: {NumberList}")
print(f"The sum of my number list is {sum(NumberList)}")

# ----------------------------------------------------------

    # One very important thing I learned from this lab was how to make/manipulate a list since the study material hadn't mentioned it up to this point.
    # Another important thing I learned in today's lab was how to index a string as I haven't had much time to practice it yet.
    # The last thing I learned today was the difference between intergers and floats, along with more practice on converting user input to interger/float values.
    # I plan on using the knowledge I've gained from today's lab to further refine my personal calculator project, along with starting my final project for Project 0.