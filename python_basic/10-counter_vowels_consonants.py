#!/usr/bin/env python3 

'''
Create a Python program to count the number of vowels and consonants in a string.
'''

def count_vowels_and_consonants(str):
    # all alphabets are consonants except aeiou - vowels 

    vowels = 'aeiouAEIOU'
    vowel_counter = 0
    consonant_counter = 0

    for ch in str:
        if ch.isalpha(): # to ensure it only consider the alphabetical char & igonore spaces and , 
            if ch in vowels:
                vowel_counter += 1
            else:
                consonant_counter += 1

    print(f"Vowels: {vowel_counter}\nConsonants: {consonant_counter}")

# call the function
message = 'A quick brown fox jumps over the lazy dog'
count_vowels_and_consonants(message)