def add(num1, num2): 
    return num1+num2

def sub(num1, num2): 
    return num1-num2

def mul(num1, num2): 
    return num1*num2

def div(num1, num2): 
    return num1/num2

def calc():
    val1 = 100
    val2 = 87
    operation = input("enter an operation: (add/sub/mul/div) ")
    if operation == "add":
        print(add(val1, val2))
    elif operation=="sub":
        print(sub(num2=val1, num1=val2))
    elif operation=="mul":
        print(mul(val1, val2))
    elif operation=="div":
        print(div(val1, val2))
    return

calc()