#!/usr/bin/env python3

# Function that checks if the character is lowercase
def islower(c):
    ascii_value = ord(c)
    if 97 <= ascii_value <= 122:
        return True
    else:
        return False

al = input("Enter any character: ")
print("{} is {}".format(al, "lower" if islower(al) else "upper"))
