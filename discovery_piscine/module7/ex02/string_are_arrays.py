#!/usr/bin/env python3

import sys
import re

number = len(sys.argv) - 1
if number == 1:
    #z_in_string = re.findall("z", sys.argv[1])
    count = 0
    for char in sys.argv[1]:
        if char == 'z':
            print("z", end='')
            count +=1
    if count == 0:
        print("none")
    else:
        print()
else:
    print("none")