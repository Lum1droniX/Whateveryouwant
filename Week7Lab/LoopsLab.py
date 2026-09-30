# Part 1: Basic While Loop
    # Write a simple loop that counts to 5 and prints each number.

        # StartNumber = 0
        # while StartNumber < 6:
        #     print(StartNumber)
        #     StartNumber += 1

# Part 2: While loop that uses user input
    # Write a while loop that asks the user something. Continue asking the user until a valid answer has been given. 

        # UserInput = input("Type the first row of letters on the keyboard.> ").lower()
        # while UserInput != "qwertyuiop":
        #     print("Invalid input!")
        #     UserInput = input("Type the first row of letters on the keyboard.> ").lower()

# Part 3: Basic For Loop
    # Write a for loop that works through a list and prints each item on the list (make your list at least 2 items)

        # GroceryList = ["Eggs", "Milk", "Bread"]
        # for Groceries in GroceryList:
        #     print(Groceries)

# Part 4: Loop with a range
    # Use a for loop with the range function. Have it print from 2 to 7. After, modify the loop to square each of the numbers.

        # for Numbers in range(2, 8):
        #     print(f"{Numbers}, {Numbers ** 2}")


# Part 5: Loop through a string
    # Create a string that is your name. Use a loop to print each character in your name and print it. 

        # FirstName = "Hayden"
        # for Letters in FirstName:
        #     print(Letters)

# Part 6: Controlling a loop
    # Use a loop to print each character in your name and print it. Use break to end the loop early

        # FirstName = "Hayden"
        # for Letters in FirstName:
        #     print(Letters)
        #     if Letters == "y":
        #         break

# Part 7: Nested Loops (Loops within Loops)
    # First create a for loop like part 4, that would print 1, 2, and 3. Now create another for loop, within that for loop that does the same thing.
    # In the second for loop, tell it to print your first loops variable, and then your seconds loops variable. Explain why its outputting what it is in a comment

        # for Numbers in range(1, 4):
        #     for Numbers2 in range(1, 4):
        #         print(Numbers, Numbers2)
        #     print(Numbers)

        # It outputs like that because it starts with the values in the nested loop for the first number in the first loop.
        # It then prints the original print() because the nested loop has finished for the first number in the first loop.
        # The same logic applies for the rest of the numbers in the first loop.