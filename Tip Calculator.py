def tip_calculator(): 
    total_amount = float(input("What is your total amount? "))
    tip_percentage = float(input("What percentage of tip are you giving? If 15%, for example, type 15. "))/100
    tip_amount = total_amount * tip_percentage
    print(f"Your total tip amount is {tip_amount}, which totals {total_amount + tip_amount}.")

tip_calculator()