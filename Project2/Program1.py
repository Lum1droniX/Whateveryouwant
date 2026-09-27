# Hayden Fillmore

    # This personal project is meant to convert 8-bit binary values to decimal and vice versa.
    # I had a stroke of inspiration while doing my networking homework to create a binary converter.
    # Most of the project was simple, although I did get stuck trying to update the DecimalSum list with 1s.
    # Turns out I just needed to update the list with indexing as .replace doesn't update the original list.
    # Came back after finishing HexConverter.py and found the floor divison / modulo method works perfectly for optimizing.

# ==========

print("================================")
print("")
print("The following code was made to convert Decimal to Binary, vice versa:")

# ==========

# This is the variable that I'll use to index the lists in the conversion calculations.
SumIndex = 7

# This loop is used to decide what value to convert and branch them into their respective inputs, along with preventing invalid inputs.
while True:
    print("")
    ConvertInput = input("Would you like to convert a Decimal or Binary value? >").upper()
    if ConvertInput == "DECIMAL":

        # This loop is used to obtain the values of a decimal input and enforce their 0 - 255 range.
        while True:
            print("")
            DecimalInput = input("What is your decimal value (0-255)? >")
            print("")
            if not 0 <= int(DecimalInput) <= 255:
                print("--==<{ Decimal value must be between 0 and 255! }>==--")
            else:
                break
        break

    elif ConvertInput == "BINARY":

        # This loop is used to obtain the values of a binary input and enforce an 8-bit value.
        while True:
            print("")
            BinaryInput = input("What is your 8-bit binary value (ex. 10110101)? >")
            print("")
            if len(BinaryInput) != 8:
                print("--==<{ Binary must be 8-bits! }>==--")
            else:
                break
        break

    else:
        print("")
        print("--==<{ Invalid input! }>==--")

print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

# ==========

# This block takes the input from above and runs the necessary calculations to convert the decimal value into binary.
if ConvertInput == "DECIMAL":

    # These lines convert the user's input into intergers while also providing the list that's to be modified and printed.
    DecimalInt = int(DecimalInput)
    DecimalSum = ["0", "0", "0", "0", "0", "0", "0", "0"]

    while DecimalInt > 0:                            # This loop repeats itself until the user's interger input reaches the negatives.
        BinaryValue = DecimalInt % 2                 # This equation takes the remainder of the input divided by 2 which can only be 1 or 0, perfect for binary.
        DecimalSum[SumIndex] = str(BinaryValue)      # This equation searches through the list starting at the last 0, then sets it equal to the result of the previous equation.
        DecimalInt //= 2                             # This equation divides the original decimal input without decimals for use in future loop calculations.
        SumIndex -= 1                                # This equation updates the indexing variable, functionally moving the calculations one digit to the left.

    print("")
    print(f"Your decimal value is {"".join(DecimalSum)} in binary!")     # "".join() is used to remove the quotation marks, commas, and spaces in the printed result.
    print("")
    
# ==========

# This block takes the input from above and runs the necessary calculations to convert the binary value into decimal.
if ConvertInput == "BINARY":

    # This is an empty list that I append the calculated values below to for the printed sum.
    BinarySum = []

    while len(BinarySum) != 8 and SumIndex > -1:     # This loop repeats itself until the length of the list equals 8 and the index variable goes below 0.
        if BinaryInput[7 - SumIndex] == "1":         # This line check if the binary input at the opposite value of the index variable is a 1, then runs the calculation if true.
            BinarySum.append(2 ** SumIndex)          # This line appends a value equal to 2^x in the BinarySum list where x is equal to the index variable.
        SumIndex -= 1                                # This equation updates the indexing variable, functionally moving the calculations one digit to the left.

    print("")
    print(f"Your binary value is {sum(BinarySum)} in decimal!")         # sum() is used to add the appended values in the list for the printed result.
    print("")