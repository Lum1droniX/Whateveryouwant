# Hayden Fillmore

    # This personal project is meant to simulate a line grapher that uses Bresenham's line algorithm to draw lines on a grid based on user input.
    # I only really want to see if I can combine the logic from my GridTest.py file with Bresenham's line algorithm to draw a line.
    # I got my inspiration for this project from a YouTube video on Minecraft redstone graphics and pulled helpful information from said video.
    # Here's the video in question: https://youtu.be/QdUkZBvfczA?si=UBnXz1XgnGINsquh
    # Ended up getting it to work, although I had to use the logic from 10:07 in the video to allow larger starting coordinates to be used.
    # I also managed to optimize the grid system into a single line of code by using list comprehension instead of a nested for loop.

# ==========

print("")
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

X1Position = int(input("What is the X position of the first point (0-30)?> "))
while not 0 <= X1Position <= 30:
    print("--==<{ Number must be between 0 and 30! }>==--")
    X1Position = int(input("What is the X position of the first point (0-30)?> "))
Y1Position = int(input("What is the Y position of the first point (0-30)?> "))
while not 0 <= Y1Position <= 30:
    print("--==<{ Number must be between 0 and 30! }>==--")
    Y1Position = int(input("What is the Y position of the first point (0-30)?> "))
print("")
X2Position = int(input("What is the X position of the second point (0-30)?> "))
while not 0 <= X2Position <= 30:
    print("--==<{ Number must be between 0 and 30! }>==--")
    X2Position = int(input("What is the X position of the second point (0-30)?> "))
Y2Position = int(input("What is the Y position of the second point (0-30)?> "))
while not 0 <= Y2Position <= 30:
    print("--==<{ Number must be between 0 and 30! }>==--")
    Y2Position = int(input("What is the Y position of the second point (0-30)?> "))

print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print("")

PlottedPoint = "{■}"

# ==========

ChangeX = abs(X2Position - X1Position)
ChangeY = abs(Y2Position - Y1Position)

StepX = 1 if X2Position > X1Position else -1
StepY = 1 if Y2Position > Y1Position else -1

SwapXY = ChangeY > ChangeX
if SwapXY:
    ChangeX, ChangeY = ChangeY, ChangeX

Error = (ChangeY * 2) - ChangeX
X = X1Position
Y = Y1Position
RowFormat = [["[ ]" for Rows in range(31)] for Columns in range(31)]

for Values in range(ChangeX + 1):
    RowFormat[Y][X] = PlottedPoint

    if Error < 0:
        Error += (ChangeY) * 2
        if SwapXY:
            Y += StepY
        else:
            X += StepX
    else:
        Error += (ChangeY * 2) - (ChangeX * 2)
        X += StepX
        Y += StepY

for Row in reversed(RowFormat):
    print("".join(Row))