#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num = number
if num < 0:
    num *= -1
else:
    num = number
if number < 0:
    result = (num % 10) * - 1
else:
    result = num % 10

if result % 10 == 0:
    print("Last digit of {} is {} and is 0".format(number, result))
elif result > 5:
    print(f"Last digit of {number} is {result} and is greater than 5")
else:
    print(f"Last digit of {number} is {result} and is less than 6 and not 0")
