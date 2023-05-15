#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """Prints all integers of a list, in reverse order.

    Args:
        my_list: The list to reverse.
    Return:
        Nothing
    """
    start = len(my_list) - 1
    step = -1

    for m in range(start, -1, step):
        print("{:d}".format(my_list[m]))
