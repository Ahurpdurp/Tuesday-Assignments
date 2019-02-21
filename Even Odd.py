def even_or_odd():
    while True:
        try:
            integer = int(input("What's your desired integer? "))
            break
        except:
            print("Please enter an integer.") 
    if integer % 2 == 0:
        print(str(integer) + " is an even integer")
        return
    elif integer % 2 == 1:
        print(str(integer) + " is an odd integer")
        return

even_or_odd()