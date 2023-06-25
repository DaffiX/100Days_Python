#!/usr/bin/env python3 
'''
Create a Python program to convert a list into a set.
'''

def list_to_set_converter(lst):
    new_set = set(lst)

    return new_set

# try our function
nations = ['USA', 'Japan', 'Nepal', 'Japan']
converted_nations = list_to_set_converter(nations)
print(converted_nations)

# list to string 
maneno = ['Hello', 'world', 'from', 'Python']
maneno_str = ' '.join(maneno)
print(maneno_str)