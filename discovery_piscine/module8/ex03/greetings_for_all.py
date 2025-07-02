#!/usr/bin/env python3

def greetings(name="noble stranger"):
    if type(name) is str:
            print(f"Hello, {name}")
    else:
        print("Error! It was not a name.")

greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)
greetings(67627)