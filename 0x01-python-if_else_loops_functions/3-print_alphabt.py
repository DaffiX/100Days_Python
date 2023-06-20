#!/usr/bin/env python3

# program that prints the ASCII alphabet in lowercase except q, e

for ch in range(97, 123):
    if chr(ch) not in ['q', 'e']:
        print(chr(ch), end="")
        
