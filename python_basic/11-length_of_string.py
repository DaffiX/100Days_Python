#!/usr/bin/env python3

'''
Create a Python program to count the number of characters in a string without using the len() function.
'''

def calc_length_string(str):
    counter = 0
    for ch in str:
        if ch.isalpha():
            counter += 1

    return counter

# test the function here 
language = "Pythona "
number_of_characters = calc_length_string(language)

print(f"The length of the string is: {number_of_characters}")