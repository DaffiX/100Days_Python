#!/usr/bin/env python3

# a program to print possible different combination of two digits

for num1 in range(1, 9):
    for num2 in range(num1 + 1, 10):
        print("{:02d}".format(num1) + ", " + "{:02d}".format(num2), end=', ')
print("{:02d}".format(89))