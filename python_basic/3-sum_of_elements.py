#!/usr/bin/env python3

"""
Create a Python program to insert an element at the end of a list.

"""
def calculate_sum(num_list):
    total = 0
    for num in num_list:
        total += num

    return total

numbers = [5, 6, 7, 8, 23, 51]
result = calculate_sum(numbers)

print(result)