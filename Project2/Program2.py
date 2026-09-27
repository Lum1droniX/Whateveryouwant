# Hayden Fillmore

    # This personal project is meant to convert 2 digit hexadecimal values to decimal and vice versa.
    # I figured this was the only logical move for the second program given the previous binary converter.
    # Got through most of this program with trial and error, although the hexadecimal to decimal logic took DAYS to troubleshoot.
    # Ended up stumbling across the .index() function while browsing through the definitions but couldn't figure it out until today.
    # Turns out the .index() function would give ValueErrors because the HexValue list numbers weren't strings, so I changed them :D
    # Did also see a hex() function which I probably should've used, but I committed to this path and don't want to redo it.

# ==========

print("================================")
print("")
print("The following code was made to convert Decimal to Hexadecimal, vice versa:")

# ==========

# This is the list that I use in later calculations and for the values in printing.
HexValues = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]

# This loop is used to decide what value to convert and branch them into their respective inputs, along with preventing invalid inputs.
while True:
    print("")
    ConvertInput = input("Would you like to convert a Decimal or Hexadecimal [Hex] value? >").upper()
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

    elif ConvertInput == "HEXADECIMAL" or ConvertInput == "HEX":

        # This loop is used to obtain the values of a 2 digit hexadecimal input and enforce an 2 digit value.
        while True:
            print("")
            HexInput = input("What is your 2-digit Hexadecimal value (00 - FF)? >").upper()
            print("")
            if len(HexInput) != 2:
                print("--==<{ Hexadecimal value must be 2 digits! }>==--")
            else:
                break
        break
    else:
        print("")
        print("--==<{ Invalid input! }>==--")

print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

# ==========

# This block takes the input from above and runs the necessary calculations to convert the decimal value into hexadecimal.
if ConvertInput == "DECIMAL":

    HexHalf1 = int(DecimalInput) // 16               # This variable floor divides the decimal input by 16 to serve as the first half of the hexadecimal result.
    HexHalf2 = int(DecimalInput) % 16                # This variable takes the remainder of said floor division to serve as the second half of the hexadecimal result.

    # This f-string takes the list value at the position of the first equation's result, followed by the second equation's result, then prints them together for the result.
    print("")
    print(f"Your decimal value is 0x{HexValues[HexHalf1]}{HexValues[HexHalf2]} in hexadecimal!")
    print("")

# ==========

# This block takes the input from above and runs the necessary calculations to convert the hexadecimal value into decimal.
if ConvertInput == "HEXADECIMAL" or ConvertInput == "HEX":

    Decimal1 = HexValues.index(HexInput[0])          # This variable searches the values list for the first occurance of the value in the first input character.
    Decimal2 = HexValues.index(HexInput[1])          # This variable searches the values list for the first occurance of the value in the second input character.
    DecimalOutput = (Decimal1 * 16) + Decimal2       # This equation takes the previous two values and multiplies them by their base value (i.e. 16^1 and 16^0).
    
    print("")
    print(f"Your hexadecimal value is {DecimalOutput} in decimal!")
    print("")