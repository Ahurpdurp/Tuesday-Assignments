def fizz_buzz():
    while True:
        try:
            number = float(input("What's your number? "))
            break
        except:
            print("Hey, that's not a number. Try again please.") 
    if number%3 == 0 and number%5 == 0: 
        print("Fizz Buzz")
    elif number%3 == 0:
        print("Fizz")
    elif number%5 == 0:
        print("Buzz")
    else:
        print("Sorry, not Fizz or Buzz")
fizz_buzz()