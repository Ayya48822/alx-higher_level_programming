#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, subtraction, multiplication, division

    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, subtraction(a, b)))
    print("{} * {} = {}".format(a, b, multiplication(a, b)))
    print("{} / {} = {}".format(a, b, division(a, b)))
