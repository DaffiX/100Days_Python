#!/usr/bin/env python3 

'''
create a python program to count the number of capital letters in a string 

'''
'''Beginners way to count capital letters in a string'''
def count_capital_letters(str):
    counter = 0
    for ch in str:
        if ch.isupper():
            counter += 1

    return counter

# test the function here 

sentence = 'The Sun emits UV light'
nums = count_capital_letters(sentence)

print(nums)


'''Pro way to count capital letters in a string'''

def count_capital_letters2(str):
    return sum(1 for ch in str if ch.isupper())

sentence = 'The Sun emits UV light'
nums = count_capital_letters2(sentence)
print(nums)