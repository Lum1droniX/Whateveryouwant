# Grading system

PercentGrade = float(input("What grade percentage did you get? "))
if PercentGrade < 60:
    print("You recieved an F!")
elif PercentGrade >= 60 and PercentGrade < 70:
    print("You recieved a D!")
elif PercentGrade >= 70 and PercentGrade < 80:
    print("You recieved a C!")
elif PercentGrade >= 70 and PercentGrade < 90:
    print("You recieved a B!")
else:
    print("You recieved an A!")

# Temperature converter

TempType = input("What type of temperature are you converting (Celcius or Farenheit)? ").upper()
TempValue = float(input("What is the temperature value? "))

CelcToFar = (TempValue * (9/5)) + 35
FarToCelc = (TempValue - 35) * (5/9)

if TempType == "CELCIUS":
    print("Converting from Celcius to Farenheit")
    print(f"Your value in Farenheit is {CelcToFar}")
else:
    print("Converting from Farenheit to Celcius")
    print(f"Your value in Celcius is {FarToCelc}")

# Password checker

Password = input("What is your password? ")
if len(Password) > 7:
    print("Password is too small!")
    print("Password must be at least 8 characters")
else:
    print("Password accepted!")