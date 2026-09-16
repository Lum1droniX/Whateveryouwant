# Hayden Fillmore

    # This code is meant to recreate an overly simplified version of the game European roulette.
    # This version of the game is only capable of Even Money and Staight Up bets, although I might add more in the future if I get bored :P
    # I've done my best to accurately recreate the probablities of a European roulette table using the random.choice() function.
    # Instead of terminating the program on invalid input by breaking the "while True" loop, I made it give an error for simplicity's sake.

import random     # This allows access to the random.choice() feature.

# ==========

print("================================")
print("")
print("The following code was made to recreate a game of roulette:")

# ==========

# This block is what recreates the colors and numbers seen on a standard European roulette table.
# It also is what lets me define how many chips to start the user out with.
NumberList = list(range(0, 37))
RedValues = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
GreenValue = 0
Balance = 20000

# This "while True:" loop is what allows the code to repeat the roll/bet cycle.
while True:

    # This block is a game over condition (bankrupt) that breaks the "while True:" loop, causing the code to end.
    if Balance <= 0:
        print("")
        print("=-=-=-=-=-=-=-=-=-=-=")
        print("You ran out of money!")
        print("=-=-=-=-=-=-=-=-=-=-=")
        print("")
        break

    # This block is used to tell the user their current balance, as well as determine how much they'll bet if anything.
    print("")
    print(f"Your current balance is {Balance}: ")
    print("")
    print("============================================================")
    BetValue = input("How much would you like to bet, or would you rather [LEAVE]? ").upper()
    print("============================================================")
    print("")

    # This block is what allows the user to leave the game by breaking the "while True:" loop, otherwise it converts the bet inputs to intergers.
    if BetValue == "LEAVE":
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print(f"Your final balance was {Balance}!")
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print("")
        break
    else:
        BetInterger = int(BetValue)

    # This line updates the Balance variable by subtracting the bet value.
    Balance -= BetInterger

# ==========

    print(f"You bet {BetInterger}, your remaining balance is {Balance}")
    print("")

    # This block determines what the user would like to bet on, converting them to intergers if they're digits and strings if they're any of the available strings.
    UserChoice = input("How would you like to bet (Odd/Even, Black/Red/Green, or 0-36)? ").upper()
    if UserChoice.isdigit():
        BetChoice = int(UserChoice)
    elif UserChoice in ["ODD", "EVEN", "BLACK", "RED", "GREEN"]:
        BetChoice = str(UserChoice)
    print("")

    # This block pulls a random number from the number list while also assigning the value both its color and odd/even conditions.
    RouletteNumber = random.choice(NumberList)
    IsGreen = RouletteNumber == GreenValue
    IsRed = RouletteNumber in RedValues
    IsBlack = not IsGreen and not IsRed
    IsEven = RouletteNumber % 2 == 0 and RouletteNumber != 0
    IsOdd = RouletteNumber % 2 != 0

    # This block just uses the color conditions to print a number for the roll results.
    if IsGreen:
        RouletteColor = "Green"
    elif IsRed:
        RouletteColor = "Red"
    else:
        RouletteColor = "Black"
    print(f"The ball landed on {RouletteNumber} {RouletteColor}")

# ==========

    # This line resets the win condition every time the code loops as to not result in improper wins/loses.
    BetWin = False

    # These win conditions check the color/odd/even conditions of the random number and compare them to the user's input.
    if BetChoice == "ODD" and IsOdd:
        BetWin = True
    elif BetChoice == "EVEN" and IsEven:
        BetWin = True
    elif BetChoice == "GREEN" and IsGreen:
        BetWin = True
    elif BetChoice == "RED" and IsRed:
        BetWin = True
    elif BetChoice == "BLACK" and IsBlack:
        BetWin = True
    elif BetChoice == RouletteNumber:
        BetWin = True
    else:
        BetWin = False

    # If the user's bet passed any win condition, the BetWin value would've become true in the last block.
    # This block then checks to see how the user won, calculates the return based on the odds, then repeats the code from the start.
    if BetWin == True:
        if BetChoice == RouletteNumber or BetChoice == "GREEN":
            PotWinnings = BetInterger * 36
            Balance += PotWinnings
        else:
            PotWinnings = BetInterger * 2
            Balance += PotWinnings
        print(f"Your {BetInterger} bet won {PotWinnings}!")

    # If the user's bet didn't pass any win condition, then the bet is lost and the code repeats from the start.
    if BetWin == False:
        print(f"Your lost your {BetInterger} bet!")