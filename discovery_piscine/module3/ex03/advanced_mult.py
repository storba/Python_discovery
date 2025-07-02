#!/usr/bin/env python3
i = 0
while i <= 10 :
    print("table of",i, end=": ")
    j = 0
    while j <= 10:
        res = i * j
        print(res, end=" ")
        j = j + 1
    i = i + 1
    print("")