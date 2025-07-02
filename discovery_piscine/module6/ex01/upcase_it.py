#!/usr/bin/env python3

import sys

number = len(sys.argv) - 1
if number == 1:
    print(sys.argv[1].upper())
else:
    print("none")