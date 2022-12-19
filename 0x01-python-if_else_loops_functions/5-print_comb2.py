#!/usr/bin/python3
number = 0
for num in range(0, 100):
    if num < 10:
        number = f"{num:02}"
    else:
	number = num
    if num < 99:
	print("{}, ".format(number), end="")
    else:
	print("{}".format(number))
