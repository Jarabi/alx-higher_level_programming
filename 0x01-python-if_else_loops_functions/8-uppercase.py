#!/usr/bin/python3

def uppercase(str):
    """Print strings in uppercase followed bby a newline"""

    for c in str:
        if c >= 'a' and c <= 'z':
            upper_char = chr(ord(c) - 32)
        else:
            upper_char = c
        print("{}".format(upper_char), end="")
    print()
