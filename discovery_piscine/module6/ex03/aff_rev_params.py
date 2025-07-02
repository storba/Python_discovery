#!/usr/bin/env python3

import sys

number = len(sys.argv) - 1
if number < 1:
    print("none")
else:
    just_param = sys.argv[1:] 
    revers_param = just_param[::-1]
    for param in revers_param:
        print(param)
