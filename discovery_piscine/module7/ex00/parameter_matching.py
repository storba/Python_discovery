#!/usr/bin/env python3

import sys

number = len(sys.argv) - 1
if number == 1:
    word = input("What was the parameter? ")
    if (word == sys.argv[1]):
        print("Good job!")
    else:
        print("Nope, sorry...")
else:
    print("none")