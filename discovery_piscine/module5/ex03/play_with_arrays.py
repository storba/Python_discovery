#!/usr/bin/env python3

array = [2, 8, 9, 48, 8, 22, -12, 2]
new_set = set()
for value in array:
    if value > 5:
        new_set.add(value + 2)
print(array)
print(new_set)