#!/usr/bin/env python3

# Function that adds two intergers and return result
def add(a, b):
    return a + b


# call the function 
num = int(input("Please key in the first number: "))
num2 = int(input("Enter number two: "))
result = add(num, num2)
print(f"{num} + {num2} = {result}")