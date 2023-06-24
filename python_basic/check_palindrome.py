#!/usr/bin/env python3

# create a program to check whether a sting is a palindrome or not 

def is_palindrome(txt):
    #reverse the string using slicing and 
    #store the revesed and then compare with original str

    rev_txt = txt[::-1]

    if rev_txt == txt:
        print("The string is Palindrome")
    else:
        print("The string is not Palindrome")

#test the function 
text = 'hannah'
is_palindrome(text)