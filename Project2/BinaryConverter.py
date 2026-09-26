# Hayden Fillmore

    # This personal project is meant to convert 8-bit binary values to decimal and vice versa.
    # I had a stroke of inspiration while doing my networking homework to create a binary converter.
    # Most of the project was simple, although I did get stuck trying to update the DecimalSum list with 1s.
    # Turns out I just needed to update the list with indexing as .replace doesn't update the original list.
    # Came back after finishing HexConverter.py and found the floor divison / modulo method works perfectly.

# ==========

print("================================")
print("")
print("The following code was made to convert Decimal to Binary, vice versa:")

# ==========

SumIndex = 7

while True:
    print("")
    ConvertInput = input("Would you like to convert a Decimal or Binary value? >").upper()
    if ConvertInput == "DECIMAL":
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

if ConvertInput == "DECIMAL":

    DecimalInt = int(DecimalInput)
    DecimalSum = ["0", "0", "0", "0", "0", "0", "0", "0"]

    while DecimalInt > 0:
        BinaryValue = DecimalInt % 2
        DecimalSum[SumIndex] = str(BinaryValue)
        DecimalInt //= 2
        SumIndex -= 1

    print("")
    print(f"Your decimal value is {"".join(DecimalSum)} in binary!")
    print("")
    
# ==========

if ConvertInput == "BINARY":

    BinarySum = []

    while len(BinarySum) != 8 and SumIndex > -1:
        if BinaryInput[7 - SumIndex] == "1":
            BinarySum.append(2 ** SumIndex)
        SumIndex -= 1

    print("")
    print(f"Your binary value is {sum(BinarySum)} in decimal!")
    print("")