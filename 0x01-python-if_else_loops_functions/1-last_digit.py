#!/usr/bin/env python3
import random 

# the last digit of a number is the number % 10
number = random.randint(-10000, 10000)
last_digit = number % 10

# check if last_digit > 5 or if == 0 or if lesss than 6
if last_digit > 5:
    print(f"Last digit of {number} is {last_digit} and is greater than 5")

elif last_digit == 0:
    print(f"Last digit of {number} is {last_digit} and is 0")

else:
    print(f"Last digit of {number} is {last_digit} and is less than 6 aand not 0")
