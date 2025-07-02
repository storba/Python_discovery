#!/usr/bin/env python3

import sys
import re

number = len(sys.argv) - 1
if number < 2:
    print("none")
else:
    keyword = sys.argv[1]
    string = sys.argv[2]
    key_in_string = re.findall(re.escape(keyword), string)
    #key_in_string = re.findall(keyword, string)
    number_keywords = len(key_in_string)
    if number_keywords == 0:
        print("none")
    else:
        print(number_keywords)