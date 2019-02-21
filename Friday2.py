def largest(numbers):
    counter = numbers[0]
    for x in numbers:
        if x > counter:
            counter = x
    print(counter)
    return

x = [1,4,2,5,6,11,2,3,-109]

largest(x)

