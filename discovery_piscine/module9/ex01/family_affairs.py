#!/usr/bin/env python3

def tolist(diction):
    return(list(diction.keys()))

def find_the_redheads(persons):
    #array = []
    #for key in persons:
    #    if persons[key] == "red":
    #        array.append(key)
    filtered = dict(filter(lambda item: item[1]=="red", persons.items()))
    return tolist(filtered)

dupont_family = {
"florian": "red",
"marie": "blond",
"virginie": "brunette",
"david": "red",
"franck": "red"
}
print(find_the_redheads(dupont_family))