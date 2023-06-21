#!/usr/bin/env python3 

def isupper(c):
    ascii_value = ord(c)
    if 65<= ascii_value <= 90:
        return True
    else:
        return False
    
upper_c = input("Engter any charachter: ")
print("{} is {}".format(upper_c, "upper" if isupper(upper_c) else "lower"))