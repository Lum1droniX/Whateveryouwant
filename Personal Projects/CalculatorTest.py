# This code is meant to be a simple calculator test just for fun

print("================================")
print("")
print("The following code was made to calculate two values given an assigned operation:")
print("")

Value1=input("What is your first value? ")
Value2=input("What is your second value? ")
Add=int(Value1)+int(Value2)
Subtract=int(Value1)-int(Value2)
Multiply=int(Value1)*int(Value2)
Divide=int(Value1)/int(Value2)

Result=input("What operation would you like to perform? (Add, Subtract, Multiply, Divide): ")
if Result=="Add":
    print("")
    print(f"The result of adding {Value1} and {Value2} is {Add}")
    print("")
    print("================================")
if Result=="Subtract":
    print("")
    print(f"The result of subtracting {Value2} from {Value1} is {Subtract}")
    print("")
    print("================================")
if Result=="Multiply":
    print("")
    print(f"The result of multiplying {Value1} and {Value2} is {Multiply}")
    print("")
    print("================================")
if Result=="Divide":
    print("")
    print(f"The result of dividing {Value1} by {Value2} is {Divide}")
    print("")
    print("================================")