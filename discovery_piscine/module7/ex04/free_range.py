#!/usr/bin/env python3

import sys

number = len(sys.argv) - 1
if number != 2:
    print("none")
else:
    try:
        num1 = int(sys.argv[1])
        num2 = int(sys.argv[2])
        if num1 >= num2:
            print("The first number must be strictly smaller than the second one.")
        else:
            numbers = [x for x in range(num1 , num2 + 1)]
            print(numbers)
    except ValueError:
        print("Parameters are not numbers")
