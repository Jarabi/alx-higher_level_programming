#!/usr/bin/python3

def remove_char_at(str, n):
    """Creates a copy of the string, removing
    the character at the position n.
    """

    if n > 0:
        copy_str = str[:n] + str[n + 1:]
    else:
        copy_str = str
    return copy_str
