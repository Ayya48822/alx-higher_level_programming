#!/usr/bin/python3
for number in range(0, 10):
    for i in range(number + 1, 10):
        if number == 8 and i == 9:
            print("{}{}".format(number, i))
        else:
            print("{}{}, ".format(number, i), end="")
