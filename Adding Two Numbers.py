def adding_two_numbers(): 
    while True:
        try:
            first_number = float(input("What's your first number? "))
            break
        except:
            print("Hey, that's not a number. Try again please.") 

    while True:
        try:
            second_number = float(input("What's your second number? "))
            break
        except:
            print("Hey, that's not a number. Try again please.")

    total_amount = first_number + second_number
    print(f"The sum of the two numbers is {total_amount}")


adding_two_numbers()


    




