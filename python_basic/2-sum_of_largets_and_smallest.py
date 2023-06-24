#!/usr/bin/env python3

"""
Create a Python program to find the sum of the largest and the smallest elements in a list.

"""

def calculate_sum(lst):
    # sort the list 
    lst.sort()
    smallest_value = lst[0]
    largest_value = lst[-1]

    total = smallest_value + largest_value

    return total

# lets test our function
numbers = [5,6,3,8,9]
result = calculate_sum(numbers)


print(result)