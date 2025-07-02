#!/usr/bin/env python3

number_input = input("Enter a number less than 25\n")
try:
    number = int(number_input)
    if number > 25:
        print("Error")
    else:
        while number <= 25:
            print("Inside the loop, my variable is", number)
            number += 1
except ValueError:
    print("Not valid number")