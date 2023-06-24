#!/usr/bin/env python3

def find_majority_element(num_list):
    for num in num_list:
        count = num_list.count(num)

    if count > len(num_list) // 2:
        return num

# given list with majority element
numbers = [1, 7, 8, 7, 7, 7]

# call the method with list as an argument
result = find_majority_element(numbers)
print(result)