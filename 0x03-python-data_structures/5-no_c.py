#!/usr/bin/python3

def no_c(my_string):
    """Removes all characters c and C from a string.

    Args:
        my_string: the string
    Return:
        The new string
    """
    new_string = ""

    for k in my_string:
        if ord(k) == 67 or ord(k) == 99:
            continue
        new_string += k
    return (new_string)
