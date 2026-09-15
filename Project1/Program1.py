# This code is meant to recreate a simplified game of European roulette.

import random

# ==========

print("================================")
print("")
print("The following code was made to recreate a game of roulette:")
print("")

NumberList = list(range(0, 37))
RedValues = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
GreenValue = 0
Balance = 20000

while True:

    if Balance <= 0:
        print("")
        print("=====================")
        print("You ran out of money!")
        print("=====================")
        print("")
        break

    print(f"Your balance is {Balance}")
    print("")
    print("============================================================")
    BetValue = input("How much would you like to bet, or would you rather [LEAVE]? ").upper()
    print("============================================================")
    print("")
    StartingBet = int(BetValue)

    if StartingBet == "LEAVE":
        print(f"Your final balance was {Balance}!")
        break

    CurrentPot = int(StartingBet)

    if StartingBet > Balance:
        print("Bet is too high!")

    Balance -= CurrentPot

# ==========

    print(f"You bet {StartingBet}, your remaining balance is {Balance}")
    print("")

    BetInput = input("How would you like to bet (Odd/Even, 1-36, Black/White/Green)? ").upper()
    if BetInput == str(range(0, 37)):
        BetValue = int(BetValue)
    else:
        BetValue = str(BetValue)

    print("")

    RouletteNumber = random.choice(NumberList)
    IsGreen = RouletteNumber == GreenValue
    IsRed = RouletteNumber in RedValues
    IsBlack = not IsGreen and not IsRed
    IsEven = RouletteNumber % 2 == 0
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
    if BetValue == "ODD" and IsOdd:
        BetWin = True
    elif BetValue == "EVEN" and IsEven:
        BetWin = True
    elif BetValue == "GREEN" and IsGreen:
        BetWin = True
    elif BetValue == "RED" and IsRed:
        BetWin = True
    elif BetValue == "BLACK" and IsBlack:
        BetWin = True
    elif BetValue == RouletteNumber:
        BetWin = True
    else:
        BetWin = False

    if BetWin == True:
        print("Your bet won!")
        if BetValue == RouletteNumber or BetValue == "GREEN":
            Balance += 35 * BetValue
        else:
            Balance += 2 * BetValue

    if BetWin == False:
        print("Your bet lost!")
