print("================================")
# This code is meant to be a simple calculator test

print("")
print("The following code was made to calculate two values given an assigned operation:")
print("")

A1=input("What is your first value? ")
A2=input("What is your second value? ")
Add=int(A1)+int(A2)
Subtract=int(A1)-int(A2)
Multiply=int(A1)*int(A2)
Divide=int(A1)/int(A2)

Result=input("What operation would you like to perform? (Add, Subtract, Multiply, Divide): ")
if Result=="Add":
    print("")
    print("The result of adding", A1,"and", A2, "is:", str(Add))
    print("")
    print("================================")
if Result=="Subtract":
    print("")
    print("The result of subtracting", A2,"from", A1, "is:", str(Subtract))
    print("")
    print("================================")
if Result=="Multiply":
    print("")
    print("The result of multiplying", A1,"and", A2, "is:", str(Multiply))
    print("")
    print("================================")
if Result=="Divide":
    print("")
    print("The result of dividing", A1,"by", A2, "is:", str(Divide))
    print("")
    print("================================")