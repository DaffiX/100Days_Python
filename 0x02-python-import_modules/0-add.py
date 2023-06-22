#!/usr/bin/env python3 

# a program that import a function and print result
if __name__ == "__main__":
    from add_0 import add

a = 1
b = 2

result = add(a, b)
print(f"{a} + {b} = {result}")
