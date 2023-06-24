#!/usr/bin/env python3 

#Create a Python program to remove all the vowels from a string.

def remove_vowels(str):

    vowels = 'aeiouAEIOU'
    for ch in str:
        if ch in vowels:
            str = str.replace(ch, "")

    return str


sentence = 'A quick brown fox jumps over the lazy dog'
result = remove_vowels(sentence)
print(result)