# Hayden Fillmore

    # This personal project is meant to simulate a grid that moves a cursor based on user input.
    # My current plan of action is to create an 11 x 11 grid with a range and for loop that prints a list.
    # As for the movement, I'll make an X/Y variable to update the lists with the crosshair position.
    # Ended up having to overhaul the graph system because the previous one couldn't move up and horizontal movement was diagonal.
    # I believe the program is in a good enough state to start work on recreating Minesweeper like I was originally planning.

# ==========

XPosition = 5
YPosition = 5
CursorPosition = "[X]"

for Row in range(0, 11):
    RowFormat = []
    for Column in range(0, 11):
        if Column == XPosition and Row == YPosition:
            RowFormat.append(CursorPosition)
        else:
            RowFormat.append("[ ]")
    print("".join(RowFormat))

# ==========

while True:

    print("")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    UserMovement = input("Where would you like to move the cursor (Up, Down, Left, Right) or leave?> ").upper()
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print("")

    if UserMovement == "UP" and YPosition > 0:
        YPosition -= 1
    elif UserMovement == "DOWN" and YPosition < 10:
        YPosition += 1
    elif UserMovement == "LEFT" and XPosition > 0:
        XPosition -= 1
    elif UserMovement == "RIGHT" and XPosition < 10:
        XPosition += 1
    elif UserMovement == "LEAVE":
        break
    else:
        print("--==<{ Invalid Input or Out Of Bounds! }>==--")
        print("")

    for Row in range(0, 11):
        RowFormat = []
        for Column in range(0, 11):
            if Column == XPosition and Row == YPosition:
                RowFormat.append(CursorPosition)
            else:
                RowFormat.append("[ ]")
        print("".join(RowFormat))