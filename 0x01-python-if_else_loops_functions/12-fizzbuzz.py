#!/usr/bin/python3
def fizzbuzz():
    number = ""
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            number = "FizzBuzz"
        elif i % 3 == 0:
            number = "Fizz"
        elif i % 5 == 0:
            number = "Buzz"
        else:
            number = f"{i}"
            if i < 100:
                print("{} ".format(number), end="")
            else:
                print("{} ".format(number), end="")
