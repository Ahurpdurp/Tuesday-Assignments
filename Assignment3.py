def prime_number():
    number = int(input("Please enter an integer "))
    if number < 2:
        print(f"{number} is not a prime number")
        return
    for x in range(2,number):
        if number%x == 0:
            print(f"{number} is not a prime number")
            return
    print(f"{number} is a prime number")
    return

prime_number() 