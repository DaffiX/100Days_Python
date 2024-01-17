#!/usr/bin/env python3

# Create a Python program to find the majority element in a list.

def find_majority_elemet(lst):
    """
    Finds the majority element i a list
    Returns the majority element if it exists, otherwise return None
    """

    counts = {} #a dict to store element counts

    # counts the occurence of each element
    for num in lst:
        counts[num] = counts.get(num, 0) + 1

    # find the element with the highest count
    majority_count = len(lst) // 2 # mojority count threshold

    for num, count in counts.items():
        if count > majority_count:
            return num

    return None # no majority element 


# test the function
numbers = [1, 7, 8, 7, 7, 7]

    
'''code like a pro'''
from collections import Counter

def find_majority_elements(lst):
    counts = Counter(lst)
    print(counts)
    majority_element = max(counts.keys(), key=counts.get, default=None)
    return majority_element if counts[majority_element] >  2 else None  
    
    
    
majority_element = find_majority_elements(numbers)

if majority_element is not None:
    print(f"The majority element is  {majority_element}")
else:
    print("There is no majority element in the list provided")