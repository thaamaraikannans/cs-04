

num1 = int(input("Enter a number 1: "))
num2 = int(input("Enter a number 2: "))
operation = input("enter a symbol (+, -, *, /) : ")

if operation == "+":
    print(num1 + num2)
elif operation == "-":
    print(num1-num2)
elif operation == "*":
    print(num1*num2)
elif operation == "/":
    if num2 != 0:
        print(num1/num2)
    else:
        print("can't divide by zero")
else:
    print("Not a valid operation")