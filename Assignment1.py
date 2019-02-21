def factorial():
    number = int(input("What's your number? "))
    while number < 0:
        number = int(input("Please choose a nonnegative number "))
    if number == 0: 
        print(f"The factorial of {number} is 1")
        return
    result = 1
    for x in range(1, number+1):
        result *= x
    print(f"The factorial of {number} is {result}")

factorial()