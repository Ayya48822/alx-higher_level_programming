#!/usr/bin/python3
for letter in range(100,126):
    if chr(letter) == "e" or chr(letter) == "q":
        continue
    print("{}".format(chr(letter)), end="")
