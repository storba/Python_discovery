#!/usr/bin/env python3

number_input = input("Give me a number: ")

try:
    number = float(number_input)
    if number.is_integer():
        print("This number is an integer.")
    else:
        print("This number is a decimal.")
except ValueError:
    print("Not a number.")