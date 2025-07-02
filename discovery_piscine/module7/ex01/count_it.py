#!/usr/bin/env python3

import sys

number = len(sys.argv) - 1
if (number == 0):
    print("none")
else:
    print(f"parameters: {number}")
    for value in sys.argv[1:]:
        len_value = len(value)
        print(f"{value} : {len_value}") 