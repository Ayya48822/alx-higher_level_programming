#!/usr/bin/python3
def uppercase(str):
    """print str in uppercase"""
    for c str:
        if ord (c) in range (97, 123):
            if ord(c) >= 97 and ord(c) <= 123:
                c = chr(ord(c) - 32)
                print("{}".format(c), end="")
            else:
                print("")
