# Hayden Fillmore

    # This personal project is meant to convert binary values to decimal and vice versa.
    # I had a stroke of inspiration while doing my networking homework to create a binary converter.

# ==========

print("================================")
print("")
print("The following code was made to convert Decimal to Binary and vice versa:")

# ==========

while True:

    print("")
    ConvertInput = input("Would you like to convert a Decimal or Binary value? ").upper()
    if ConvertInput == "DECIMAL":
        while True:
            print("")
            DecimalInput = int(input("What is your decimal value (0-255)? "))
            print("")
            if not 0 <= DecimalInput <= 255:
                print("Decimal value must be between 0 and 255!")
            else:
                break
        break
    elif ConvertInput == "BINARY":
        while True:
            print("")
            BinaryInput = input("What is your 8-bit binary value (ex. 10110101)? ")
            if len(BinaryInput) != 8:
                print("Binary must be 8-bits!")
            else:
                break
        break
    else:
        print("")
        print("Invalid input!")

# ==========

if ConvertInput == "DECIMAL":

    DecimalValue = int(DecimalInput)
    DecimalSum = []

    while True:

        if DecimalValue >= 128:
            DecimalSum.append("1")
            DecimalValue -= 128
        if 128 < DecimalValue <= 64:
            DecimalSum.append("1")
            DecimalValue -= 64
        if 64 < DecimalValue <= 32:
            DecimalSum.append("1")
            DecimalValue -= 32
        if 32 < DecimalValue <= 16:
            DecimalSum.append("1")
            DecimalValue -= 16
        if 16 < DecimalValue <= 8:
            DecimalSum.append("1")
            DecimalValue -= 8
        if 8 < DecimalValue <= 4:
            DecimalSum.append("1")
            DecimalValue -= 4
        if 4 < DecimalValue <= 2:
            DecimalSum.append("1")
            DecimalValue -= 2
        if 2 < DecimalValue <= 1:
            DecimalSum.append("1")
            DecimalValue -= 1
        elif DecimalValue == 0:
            break
        else:
            DecimalSum.append("0")

    print("")
    print(f"Your decimal value is {"".join(DecimalSum)} in binary!")
    print("")
    
# ==========

if ConvertInput == "BINARY":

    BinarySum = []

    if BinaryInput[0] == "1":
        BinarySum.append(128)
    if BinaryInput[1] == "1":
        BinarySum.append(64)
    if BinaryInput[2] == "1":
        BinarySum.append(32)
    if BinaryInput[3] == "1":
        BinarySum.append(16)
    if BinaryInput[4] == "1":
        BinarySum.append(8)
    if BinaryInput[5] == "1":
        BinarySum.append(4)
    if BinaryInput[6] == "1":
        BinarySum.append(2)
    if BinaryInput[7] == "1":
        BinarySum.append(1)
    else:
        BinarySum.append(0)

    print("")
    print(f"Your binary value is {sum(BinarySum)} in decimal!")
    print("")
