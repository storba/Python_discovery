#!/usr/bin/env python3
import sys

def shrink(str):
    return(str[0:8])
def enlarge(str):
    str_z = 'Z' * (8 - len(str))
    return str + str_z

number = len(sys.argv) - 1
if number == 0:
    print("none")
else:
    for value in sys.argv[1:]:
        if len(value) == 8:
            print(value)
        elif len(value) < 8:
            print(enlarge(value))
        else:
            print(shrink(value))