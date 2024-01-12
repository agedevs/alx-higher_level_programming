#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
oderRange = ""

if (last_digit > 5 and number > 0):
    oderRange = "greater than 5"
    print(f"Last digit of {number} is {last_digit} and is {oderRange}")
elif (last_digit == 0):
    oderRange = "0"
    print(f"Last digit of {number} is {last_digit} and is {oderRange}")
else:
    oderRange = "less than 6 and not 0"
    print(f"Last digit of {number} is -{last_digit} and is {oderRange}")
