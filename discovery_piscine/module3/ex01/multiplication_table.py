#!/usr/bin/env python3
number_input = input("Enter a number\n")
try:
    number = int(number_input)
    i = 0
    while i <= 9:
        result = i * number
        print(f"{i} x {number} = {result}")
        i = i + 1
except ValueError:
    print("Not valid number")