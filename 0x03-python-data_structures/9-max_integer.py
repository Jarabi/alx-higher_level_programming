#!/usr/bin/python3

def max_integer(my_list=[]):
    """Finds the biggest integer of a list.

    Args:
        my_list: Integer list
    Return:
        Largest integer
    """
    if len(my_list) == 0:
        return (None)

    max_int = my_list[0]

    for el in my_list:
        if el > max_int:
            max_int = el
    return (max_int)
