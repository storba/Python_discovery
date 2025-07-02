#!/usr/bin/env python3
import sys

def downcase_it(st):
    return st.lower()

number = len(sys.argv) - 1
if number == 0:
    print("none")
else:
    for value in sys.argv[1:]:
        print(downcase_it(value))