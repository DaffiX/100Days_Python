#!/usr/bin/env python3 
import random 

# script that print the number if positive or negative
number = random.randint(-10, 10)

if number > 0:
    print(f"{number} is positive")

elif number < 0:
    print(f"{number} is negative")

else:
    print(f"{number} is zeor")
