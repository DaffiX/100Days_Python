#!/usr/bin/env python3

# a fuction that print the last digit of a num
def print_last_digit(number):
    last_digit = number % 10
    return last_digit

# let call the function
number = int(input("What your number: "))
result = print_last_digit(number)
print(result)