#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """Prints all integers of a list, in reverse order.

    Args:
        my_list: The list to reverse.
    Return:
        Nothing
    """
    if my_list:
        for m in my_list[::-1]:
            print("{:d}".format(m))
