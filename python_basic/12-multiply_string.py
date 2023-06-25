#!/usr/bin/env python3

'''
Create a Python program to multiply two strings as integers.
'''

# fuction that multipy two string and return an int
def calc_int_str(a, b):
    new_a = int(a)
    new_b = int(b)

    return new_a * new_b


value1 = '10'
value2 = '10'

result = calc_int_str(value1, value2)
print(result)