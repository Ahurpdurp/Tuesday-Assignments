def pyramid():
    levels = int(input("How many levels do you want your pyramid to be? Positive integers only please: "))
    for x in range(levels):
        row = " " * (levels - 1 - x) + "*" * (x * 2 + 1)
        print(row)
        


pyramid()

