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

NumberList = list(range(0, 37))
RedValues = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
GreenValue = 0
Balance = 20000

while True:

    if Balance <= 0:
        print("")
        print("=-=-=-=-=-=-=-=-=-=-=")
        print("You ran out of money!")
        print("=-=-=-=-=-=-=-=-=-=-=")
        print("")
        break

    print("")
    print(f"Your current balance is {Balance}: ")
    print("")
    print("============================================================")
    BetValue = input("How much would you like to bet, or would you rather [LEAVE]? ").upper()
    print("============================================================")
    print("")

    if BetValue == "LEAVE":
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print(f"Your final balance was {Balance}!")
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print("")
        break
    else:
        BetInterger = int(BetValue)

    Balance -= BetInterger

# ==========

    print(f"You bet {BetInterger}, your remaining balance is {Balance}")
    print("")

    UserChoice = input("How would you like to bet (Odd/Even, Black/Red/Green, or 0-36)? ").upper()
    if UserChoice.isdigit():
        BetChoice = int(UserChoice)
    elif UserChoice in ["ODD", "EVEN", "BLACK", "RED", "GREEN"]:
        BetChoice = str(UserChoice)

    print("")

    RouletteNumber = random.choice(NumberList)
    IsGreen = RouletteNumber == GreenValue
    IsRed = RouletteNumber in RedValues
    IsBlack = not IsGreen and not IsRed
    IsEven = RouletteNumber % 2 == 0 and RouletteNumber != 0
    IsOdd = RouletteNumber % 2 != 0

    if IsGreen:
        RouletteColor = "Green"
    elif IsRed:
        RouletteColor = "Red"
    else:
        RouletteColor = "Black"

    print(f"The ball landed on {RouletteNumber} {RouletteColor}")

    # ==========

    BetWin = False

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

    if BetWin == True:
        if BetChoice == RouletteNumber or BetChoice == "GREEN":
            PotWinnings = BetInterger * 36
            Balance += PotWinnings
        else:
            PotWinnings = BetInterger * 2
            Balance += PotWinnings
        print(f"Your {BetInterger} bet won {PotWinnings}!")

    if BetWin == False:
        print(f"Your lost your {BetInterger} bet!")