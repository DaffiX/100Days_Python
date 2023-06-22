#!/usr/bin/env python3

"""
    The sys module provides access to the command-line arguments and other variables used or maintained by the interpreter

"""
import sys

def print_arguments():
    # because sys.argv[0] - is the name of the script itself
    num_arguments = len(sys.argv) - 1

    # let slice 
    arguments = sys.argv[1:] 

    print("Number of arguments:", num_arguments)
    print("List of arguments:", arguments)

# call the function - python3 program.py arg1 arg2 arg3
print_arguments()