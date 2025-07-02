#!/usr/bin/env python3

def array_of_names(persons):
    array = []
    for key in persons:
        array.append(key.capitalize() + " " + persons[key].capitalize())
    return array

persons = {
"jean": "valjean",
"grace": "hopper",
"xavier": "niel",
"fifi": "brindacier"
}
print(array_of_names(persons))