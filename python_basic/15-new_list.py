#!/usr/bin/env python3
'''
Create a Python program to create a new list from an existing list of strings by copying only those elements that start with a consonant.
'''
def copy_consonant_elements(lst):
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    new_lst = [] # initialize an empty list to hold new list

    for word in lst:
        # check to satisfy both conditions 
        if word and word[0] in consonants:
            #append that word to the list 

            new_lst.append(word)

    return new_lst

# test case 
original_list = ['apple', 'banana', 'pineapple', 'mango', 'watermelon']
new_list = copy_consonant_elements(original_list)
print(new_list)

# using list comprehension method 

def copy_consonants_elements(lst):
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    new_list = [word for word in lst if word and word[0] in consonants]

    return new_list

# you may run the test here 