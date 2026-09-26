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

HexValues = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]

while True:

    print("")
    ConvertInput = input("Would you like to convert a Decimal or Hexadecimal [Hex] value? >").upper()
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
    elif ConvertInput == "HEXADECIMAL" or ConvertInput == "HEX":
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

if ConvertInput == "DECIMAL":

    HexHalf1 = int(DecimalInput) // 16
    HexHalf2 = int(DecimalInput) % 16

    print("")
    print(f"Your decimal value is 0x{HexValues[HexHalf1]}{HexValues[HexHalf2]} in hexadecimal!")
    print("")

# ==========

if ConvertInput == "HEXADECIMAL" or ConvertInput == "HEX":

    Decimal1 = HexValues.index(HexInput[0])
    Decimal2 = HexValues.index(HexInput[1])
    
    DecimalOutput = (Decimal1 * 16) + Decimal2
    
    print("")
    print(f"Your hexadecimal value is {DecimalOutput} in decimal!")
    print("")