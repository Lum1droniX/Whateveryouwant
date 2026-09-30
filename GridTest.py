# Hayden Fillmore

    # This personal project is meant to simulate a grid that moves a cursor based on user input
    # My current plan of action is to create an 11 x 11 grid with a range and for loop that prints a list.
    # As for the movement, I'll make an X/Y variable to update the lists with the crosshair position

# ==========

XPosition = 4
YPosition = 4
CursorPosition = "[X]"

while True:

    UserMovement = input("Where would you like to move the cursor (Up, Down, Left, Right)?> ").upper()
    GridFormat = ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"]


    for Columns in range(0, 9):
        print("".join(GridFormat))
        if Columns == XPosition:
            GridFormat[XPosition] = CursorPosition
        elif range(0, 9) == YPosition:
            range[YPosition] = CursorPosition

    if UserMovement == "UP":
        YPosition += 1
    elif UserMovement == "DOWN":
        YPosition -= 1
    elif UserMovement == "LEFT":
        XPosition -= 1
    elif UserMovement == "RIGHT":
        XPosition += 1
    else:
        print("--==<{ Invalid Input! }>==--")
