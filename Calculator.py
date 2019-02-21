def calculator():
    input1 = float(input("What's your first number? "))
    input2 = input("What operand do you want between the following: +, -, *, or / ")
    while input2 not in ("+", "-", "*", "/"):
        input2 = input("Please choose +, -, *, or / ")
    input3 = float(input("What's your second number? "))
    if input2 == "+":
        addition(input1,input3)
        return
    elif input2 == "-":
        subtraction(input1,input3)
        return
    elif input2 == "*":
        multiplication(input1,input3)
        return
    elif input2 == "/":
        division(input1, input3)
        return


def addition(a, b):
    print("Your  answer is " + str(a + b))

def subtraction(a, b):
    print("Your  answer is " + str(a - b))

def multiplication(a, b):
    print("Your  answer is " + str(a*b))

def division(a, b):   
    print("Your  answer is " + str(a/b))      

calculator()