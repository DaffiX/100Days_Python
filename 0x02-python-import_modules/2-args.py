#!/usr/bin/env python3 
import sys

# a program that print the command argv
if __name__ == "__main__":
    num_arguments = len(sys.argv) - 1

    if num_arguments == 0:
        print("0 arguments.")

    elif num_arguments == 1:
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))
    else:
        print("{} arguments:".format(num_arguments))
        for i in range(1, num_arguments + 1):
            print("{}: {}".format(i, sys.argv[i]))