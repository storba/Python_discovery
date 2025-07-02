#!/usr/bin/env python3

first_number_input = input("Give me the first number: ")
second_number_input = input("Give me the second number: ")
print("Thank you!")
try:
    first_number = int(first_number_input)
    second_number = int(second_number_input)
    print(f"{first_number} + {second_number} = {first_number + second_number}")
    print(f"{first_number} - {second_number} = {first_number - second_number}")
    print(f"{first_number} / {second_number} = {int(first_number / second_number)}")
    print(f"{first_number} * {second_number} = {first_number * second_number}")
except ValueError:
    print("Not valid number")
except ZeroDivisionError:
    print("Division on zero")