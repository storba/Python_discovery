#!/usr/bin/env python3

import sys

number = len(sys.argv) - 1
if number < 1:
    print("none")
else:
    for param in sys.argv[1:]:
        if param.find("ism",len(param)-3) == -1:
            print(f"{param}ism")