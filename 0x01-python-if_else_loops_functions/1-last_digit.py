#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num = number
if num < 0
num *= -1
else:
    num = number
    if number < 0:
        last d = (num % 10) * -1
    else:
        last d = num % 10

if last d % 10 == 0:
    print(f"Last digit of {number} is {last d} and is 0")
elif last d > 5:
    print(f"Last digit of {number} is {last d} and is greater than 5")
else:
    print(f"Last digit of {number} is {last d} and is less than 6 and not 0")
