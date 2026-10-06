# Hayden Fillmore

    # This personal project is meant to simulate a line grapher that uses Bresenham's line algorithm to draw lines on a grid based on user input.
    # I only really want to see if I can combine the logic from my GridTest.py file with Bresenham's line algorithm to draw a line.
    # I got my inspiration for this project from a YouTube video on Minecraft redstone graphics and pulled helpful information from said video.
    # Here's the video in question: https://youtu.be/QdUkZBvfczA?si=UBnXz1XgnGINsquh

# ==========

print("")
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
X1Position = int(input("What is the X position of the first point (0-15)?> "))
Y1Position = int(input("What is the Y position of the first point (0-15)?> "))
print("")
X2Position = int(input("What is the X position of the second point (0-15)?> "))
Y2Position = int(input("What is the Y position of the second point (0-15)?> "))
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print("")

CursorPosition = "[■]"

# ==========

def BresenhamLine(X1Position, Y1Position, X2Position, Y2Position):
    Error = -(X2Position - X1Position)
    Slope = (Y2Position - Y1Position) * 2

    X = X1Position
    Y = (16 - Y1Position)

    for Row in range(0, 16):
        RowFormat = []
        for Column in range(0, 16):
            RowFormat.append(CursorPosition) if Column == X or Row == Y else RowFormat.append("[ ]")
        print("".join(RowFormat))

    while X < X2Position:
        X += 1
        Error += Slope

        if Error >= 0:
            Y += 1
            Error -= (X2Position - X1Position) * 2

            for Row in range(0, 16):
                RowFormat = []
                for Column in range(0, 16):
                    RowFormat.append(CursorPosition) if Column == X or Row == Y else RowFormat.append("[ ]")
                print("".join(RowFormat))

# ==========

print(BresenhamLine(X1Position, Y1Position, X2Position, Y2Position))